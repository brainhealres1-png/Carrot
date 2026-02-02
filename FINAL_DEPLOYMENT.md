# 최종 배포 체크리스트

## 1. S3에 올릴 파일

**파일:** `index_static.html`

**단계:**
1. `index_static.html`을 `index.html`로 이름 변경
2. S3 버킷 `aaaabbbbaaababaa`에 업로드
3. S3 정적 웹사이트 설정:
   - 버킷 → Properties → Static website hosting
   - Index document: `index.html`
   - 저장

**결과:** https://aaaabbbbaaababaa.s3-website.ap-northeast-2.amazonaws.com

---

## 2. Lambda에 올릴 파일

**파일:** `lambda_deploy/lambda_function.zip`

**단계:**
1. AWS Lambda 콘솔 → `carrot` 함수 선택
2. Code 탭 → Upload from → .zip file
3. `lambda_function.zip` 업로드
4. Deploy 클릭

**Lambda 환경변수 설정:**
- Configuration 탭 → Environment variables → Edit
- 추가:
  ```
  SUPABASE_URL = https://hfznugbfbiytsbncdiyh.supabase.co
  SUPABASE_KEY = sb_secret_dpYtf0Quq-nVH4G0hr4v7Q_gpmDKHT2
  ```
- Save 클릭

---

## 3. Supabase 테이블 생성

**파일:** `create_table.sql`

**단계:**
1. Supabase 대시보드 → SQL Editor
2. `create_table.sql` 내용 복사
3. 실행

---

## 최종 구조

```
S3 (프론트엔드)
└── index.html
    └── Lambda API 호출
        └── Supabase DB 저장

Lambda (백엔드)
└── lambda_function.zip
    ├── lambda_handler.py
    ├── supabase/
    └── dotenv/

API Gateway
└── POST /carrot-api → Lambda
└── GET /carrot-api → Lambda

Supabase
└── names 테이블
```

---

## 배포 순서

1. ✓ Lambda 함수 생성 (carrot)
2. ✓ API Gateway 생성 (carrot-api)
3. ✓ /carrot-api 리소스 생성
4. ✓ POST, GET 메서드 추가
5. ✓ CORS 활성화
6. ✓ prod 스테이지 배포
7. → **Lambda ZIP 업로드** (지금)
8. → **Lambda 환경변수 설정** (지금)
9. → **Supabase 테이블 생성** (지금)
10. → **S3에 index.html 업로드** (지금)

---

## 테스트

1. S3 웹사이트 URL 접속
2. 이름 입력 후 제출
3. Supabase 대시보드에서 names 테이블 확인
4. 데이터가 저장되었는지 확인
