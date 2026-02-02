# API Gateway 생성 가이드

## 1. API Gateway 콘솔 열기

AWS 콘솔 → API Gateway → **Create API**

---

## 2. API 유형 선택

### 선택할 것: **REST API**
- 다른 옵션들은 선택하지 않음
- "Build" 버튼 클릭

---

## 3. API 생성 설정

### 기본 정보
- **API name**: `carrot-api`
- **Description**: Carrot name storage API
- **Endpoint Type**: Regional (기본값)

### 생성 버튼 클릭

---

## 4. 리소스 생성

### 4-1. 루트 리소스에서 새 리소스 생성
1. 왼쪽 메뉴 → **Resources**
2. "/" (루트) 선택
3. **Create Resource** 클릭

### 4-2. 리소스 설정
- **Resource Name**: `names`
- **Resource Path**: `/names` (자동 입력됨)
- **Create Resource** 클릭

---

## 5. 메서드 추가

### 5-1. POST 메서드 추가
1. `/names` 리소스 선택
2. **Create Method** → **POST** 선택
3. **Integration type**: Lambda Function
4. **Lambda Function**: `carrot-api` 선택
5. **Save** 클릭
6. "Add Permission to Lambda Function" 팝업 → **OK**

### 5-2. GET 메서드 추가
1. `/names` 리소스 선택
2. **Create Method** → **GET** 선택
3. **Integration type**: Lambda Function
4. **Lambda Function**: `carrot-api` 선택
5. **Save** 클릭
6. "Add Permission to Lambda Function" 팝업 → **OK**

---

## 6. CORS 활성화

### 6-1. CORS 설정
1. `/names` 리소스 선택
2. **Actions** → **Enable CORS and replace CORS headers**
3. 팝업에서 모든 메서드 선택 (POST, GET, OPTIONS)
4. **Enable CORS and replace existing CORS headers** 클릭
5. "Yes, replace existing values" 클릭

---

## 7. API 배포

### 7-1. 배포
1. **Actions** → **Deploy API**
2. **Deployment stage**: `prod` (새로 생성)
3. **Deploy** 클릭

### 7-2. Invoke URL 확인
배포 완료 후:
1. 왼쪽 메뉴 → **Stages**
2. **prod** 클릭
3. 상단에 **Invoke URL** 표시됨

예시:
```
https://abc123xyz.execute-api.us-east-1.amazonaws.com/prod
```

---

## 8. .env 파일 업데이트

Invoke URL을 복사해서 .env에 입력:

```
SUPABASE_URL=https://hfznugbfbiytsbncdiyh.supabase.co
SUPABASE_KEY=sb_secret_dpYtf0Quq-nVH4G0hr4v7Q_gpmDKHT2
LAMBDA_API_URL=https://abc123xyz.execute-api.us-east-1.amazonaws.com/prod/names
```

---

## 최종 구조

```
API Gateway: carrot-api
└── /names (리소스)
    ├── POST (Lambda: carrot-api)
    ├── GET (Lambda: carrot-api)
    └── OPTIONS (CORS)
```

---

## 체크리스트

- [ ] REST API 생성
- [ ] API 이름: carrot-api
- [ ] /names 리소스 생성
- [ ] POST 메서드 추가 (Lambda 연결)
- [ ] GET 메서드 추가 (Lambda 연결)
- [ ] CORS 활성화
- [ ] prod 스테이지에 배포
- [ ] Invoke URL 복사
- [ ] .env 파일 업데이트
