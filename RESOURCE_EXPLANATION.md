# API Gateway 리소스란?

## 간단한 설명

**리소스 = API의 경로(URL 주소)**

---

## 예시

### 웹사이트 URL 구조
```
https://example.com/users
https://example.com/products
https://example.com/orders
```

### API Gateway 리소스 구조
```
API Gateway: carrot-api
├── / (루트)
└── /names ← 우리가 만드는 리소스
```

---

## 우리의 경우

### 최종 API 주소
```
https://abc123xyz.execute-api.us-east-1.amazonaws.com/prod/names
                                                              ↑
                                                         이 부분이 리소스
```

### 리소스 설정
- **Resource Name**: `names` (이름)
- **Resource Path**: `/names` (경로)

---

## 리소스와 메서드의 관계

```
리소스: /names
├── POST 메서드 → 이름 저장 (데이터 생성)
└── GET 메서드 → 모든 이름 조회 (데이터 읽기)
```

### 실제 사용
```
POST /names → 새로운 이름 저장
GET /names → 저장된 모든 이름 조회
```

---

## 다른 예시

### 블로그 API라면
```
API Gateway: blog-api
├── /posts (리소스)
│   ├── POST → 새 글 작성
│   └── GET → 모든 글 조회
├── /comments (리소스)
│   ├── POST → 댓글 작성
│   └── GET → 모든 댓글 조회
└── /users (리소스)
    ├── POST → 사용자 등록
    └── GET → 모든 사용자 조회
```

---

## 우리 프로젝트에서

### 리소스 생성 단계
1. API Gateway 콘솔 열기
2. `carrot-api` API 선택
3. 왼쪽 메뉴 → **Resources**
4. "/" (루트) 선택
5. **Create Resource** 클릭
6. **Resource Name** 입력: `names`
7. **Create Resource** 클릭

### 결과
```
carrot-api
└── /names ← 생성됨
```

---

## 정리

- **리소스** = API의 경로 (예: /names)
- **메서드** = 리소스에서 할 수 있는 작업 (POST, GET, PUT, DELETE 등)
- **Lambda** = 메서드가 실행할 함수

### 흐름
```
사용자 요청
  ↓
POST /names (메서드 + 리소스)
  ↓
API Gateway (라우팅)
  ↓
Lambda 함수 실행 (carrot-api)
  ↓
Supabase DB에 저장
  ↓
응답 반환
```
