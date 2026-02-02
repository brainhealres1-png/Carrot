# AWS 배포 가이드

## 1. 프론트엔드 S3 배포

### 빌드
```powershell
reflex export
```

### S3 업로드
- S3 버킷: `aaaabbbbaaababaa`
- 정적 웹사이트 호스팅 활성화
- `.web/build/client` 폴더의 모든 파일 업로드

### S3 버킷 정책
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::aaaabbbbaaababaa/*"
    }
  ]
}
```

---

## 2. Lambda 백엔드 배포

### 준비 단계

1. **Lambda 함수 생성**
   - 런타임: Python 3.11
   - 함수명: carrot-api

2. **환경변수 설정** (Lambda 콘솔)
   ```
   SUPABASE_URL=https://hfznugbfbiytsbncdiyh.supabase.co
   SUPABASE_KEY=sb_secret_dpYtf0Quq-nVH4G0hr4v7Q_gpmDKHT2
   ```

3. **배포 패키지 생성**
   ```powershell
   # 1. 임시 폴더 생성
   mkdir lambda_package
   cd lambda_package
   
   # 2. 의존성 설치
   pip install -r ..\lambda_requirements.txt -t .
   
   # 3. lambda_handler.py 복사
   copy ..\lambda_handler.py .
   
   # 4. zip 파일 생성
   Compress-Archive -Path * -DestinationPath lambda_function.zip
   ```

4. **Lambda에 업로드**
   - AWS Lambda 콘솔에서 lambda_function.zip 업로드
   - 핸들러: lambda_handler.lambda_handler

---

## 3. API Gateway 설정

1. **API 생성**
   - REST API 생성
   - 리소스명: /names

2. **메서드 설정**
   - POST, GET 메서드 추가
   - Lambda 함수와 연결

3. **CORS 활성화**
   - 리소스 선택 → Actions → Enable CORS
   - 모든 메서드에 CORS 활성화

4. **배포**
   - Stage: prod
   - API 엔드포인트 URL 복사

---

## 4. 프론트엔드 수정

`code.py`의 다음 부분을 수정:

```python
# Lambda API 엔드포인트로 변경
LAMBDA_API_URL = "https://YOUR_API_GATEWAY_URL/names"
```

실제 API Gateway URL로 교체 후 `reflex export` 다시 실행

---

## 5. Supabase 테이블 생성

Supabase 대시보드 → SQL Editor에서 `create_table.sql` 실행

---

## 파일 구조

```
Carrot/
├── lambda_handler.py          # Lambda 함수
├── lambda_requirements.txt     # 의존성
├── create_table.sql           # DB 테이블
├── .env                        # Supabase 정보
├── code/
│   └── code.py               # 프론트엔드 (수정 필요)
└── AWS_DEPLOYMENT.md         # 이 파일
```

---

## 환경변수 (.env)

```
SUPABASE_URL=https://hfznugbfbiytsbncdiyh.supabase.co
SUPABASE_KEY=sb_secret_dpYtf0Quq-nVH4G0hr4v7Q_gpmDKHT2
```

Lambda 환경변수에도 동일하게 설정해야 합니다.
