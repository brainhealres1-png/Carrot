# API Gateway 주소 얻기

## 1. API Gateway 콘솔에서 확인

### 방법 1: Stages에서 확인 (가장 쉬움)
1. AWS 콘솔 → API Gateway
2. 생성한 API 선택 (예: carrot-api)
3. 왼쪽 메뉴 → **Stages**
4. **prod** 스테이지 클릭
5. 상단에 **Invoke URL** 표시됨

예시:
```
https://abc123xyz.execute-api.us-east-1.amazonaws.com/prod
```

### 방법 2: Dashboard에서 확인
1. API Gateway 콘솔
2. 생성한 API 선택
3. Dashboard 탭
4. **Invoke this API** 섹션에서 URL 확인

---

## 2. 전체 엔드포인트 URL 구성

### 기본 형식
```
https://{API_ID}.execute-api.{REGION}.amazonaws.com/{STAGE}/names
```

### 예시
```
https://abc123xyz.execute-api.us-east-1.amazonaws.com/prod/names
```

### 각 부분 설명
- `abc123xyz` = API ID (자동 생성)
- `us-east-1` = AWS 리전
- `prod` = 스테이지명
- `names` = 리소스 경로

---

## 3. .env 파일에 입력

API Gateway 주소를 얻은 후:

```
SUPABASE_URL=https://hfznugbfbiytsbncdiyh.supabase.co
SUPABASE_KEY=sb_secret_dpYtf0Quq-nVH4G0hr4v7Q_gpmDKHT2
LAMBDA_API_URL=https://abc123xyz.execute-api.us-east-1.amazonaws.com/prod/names
```

---

## 4. 프론트엔드 빌드 및 배포

.env 파일 수정 후:

```powershell
# 프론트엔드 빌드
reflex export

# .web/build/client 폴더를 S3에 업로드
# 버킷명: aaaabbbbaaababaa
```

---

## 체크리스트

- [ ] Lambda 함수 생성 및 배포
- [ ] API Gateway 생성
- [ ] /names 리소스 생성
- [ ] POST, GET 메서드 추가
- [ ] CORS 활성화
- [ ] API 배포 (prod 스테이지)
- [ ] **Invoke URL 복사** ← 여기서 주소 얻음
- [ ] .env 파일에 LAMBDA_API_URL 입력
- [ ] reflex export 실행
- [ ] S3에 업로드
