# Lambda 배포 체크리스트

## Lambda에 올려야 할 파일

### 1. 필수 파일
- `lambda_handler.py` - Lambda 함수 코드
- `lambda_requirements.txt` - Python 의존성

### 2. 배포 패키지 생성 방법

```powershell
# 1. 임시 폴더 생성
mkdir lambda_deploy
cd lambda_deploy

# 2. 의존성 설치
pip install -r ..\lambda_requirements.txt -t .

# 3. lambda_handler.py 복사
copy ..\lambda_handler.py .

# 4. zip 파일 생성
Compress-Archive -Path * -DestinationPath lambda_function.zip

# 5. AWS Lambda 콘솔에서 lambda_function.zip 업로드
```

---

## Lambda 콘솔 설정

### 기본 정보
- **함수명**: carrot-api
- **런타임**: Python 3.11
- **핸들러**: lambda_handler.lambda_handler
- **메모리**: 128 MB
- **타임아웃**: 30초

### 환경변수 설정 (필수!)
Lambda 콘솔 → Configuration → Environment variables

```
SUPABASE_URL = https://hfznugbfbiytsbncdiyh.supabase.co
SUPABASE_KEY = sb_secret_dpYtf0Quq-nVH4G0hr4v7Q_gpmDKHT2
```

---

## API Gateway 설정

### 1. API 생성
- 유형: REST API
- API 이름: carrot-api

### 2. 리소스 생성
- 리소스 경로: /names

### 3. 메서드 추가
- POST 메서드 → Lambda 함수 선택 (carrot-api)
- GET 메서드 → Lambda 함수 선택 (carrot-api)

### 4. CORS 활성화
- /names 리소스 선택
- Actions → Enable CORS and replace CORS headers
- 모든 메서드 선택 후 Enable

### 5. 배포
- Actions → Deploy API
- Stage: prod
- **API 엔드포인트 URL 복사** (예: https://abc123.execute-api.us-east-1.amazonaws.com/prod)

---

## 프론트엔드 수정

`code.py` 수정:

```python
# 이 부분을 API Gateway 엔드포인트로 변경
LAMBDA_API_URL = "https://YOUR_API_GATEWAY_URL/names"
```

예시:
```python
LAMBDA_API_URL = "https://abc123.execute-api.us-east-1.amazonaws.com/prod/names"
```

---

## 빠진 정보 체크리스트

- [ ] SUPABASE_URL (✓ 있음)
- [ ] SUPABASE_KEY (✓ 있음)
- [ ] API Gateway 엔드포인트 URL (⚠️ 배포 후 생성됨)
- [ ] S3 버킷명 (⚠️ 사용자가 정해야 함)
- [ ] AWS 리전 (⚠️ 기본값: us-east-1)

---

## 최종 확인

1. ✓ lambda_handler.py - Lambda 함수 코드
2. ✓ lambda_requirements.txt - 의존성 (supabase, python-dotenv)
3. ✓ create_table.sql - Supabase 테이블
4. ✓ .env - Supabase 정보
5. ✓ code.py - 프론트엔드 (API URL 수정 필요)
6. ✓ AWS_DEPLOYMENT.md - 배포 가이드
