# 최종 간단 설정

## 1. S3에 올릴 파일

**파일:** `index.html`

```powershell
# S3 버킷 aaaabbbbaaababaa에 업로드
```

---

## 2. Lambda에 올릴 파일

**파일:** `lambda_function.zip`

### 생성 방법:

```powershell
cd D:\Github\Carrot
mkdir lambda_simple
cd lambda_simple

# lambda_handler_lite.py를 lambda_function.py로 복사
copy ..\lambda_handler_lite.py lambda_function.py

# ZIP 생성
Compress-Archive -Path lambda_function.py -DestinationPath lambda_function.zip
```

### AWS Lambda 콘솔:

1. `carrot` 함수 선택
2. Code 탭 → Upload from → .zip file
3. `lambda_function.zip` 업로드
4. Handler: `lambda_function.lambda_handler`
5. Deploy

---

## 3. Lambda 환경변수

Configuration 탭 → Environment variables:

```
SUPABASE_URL = https://hfznugbfbiytsbncdiyh.supabase.co
SUPABASE_KEY = sb_secret_dpYtf0Quq-nVH4G0hr4v7Q_gpmDKHT2
```

---

## 4. Supabase 테이블

SQL Editor에서 실행:

```sql
CREATE TABLE IF NOT EXISTS names (
  id BIGSERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

ALTER TABLE names ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow public insert" ON names
  FOR INSERT WITH CHECK (true);
```

---

## 완료!

- S3: index.html 업로드
- Lambda: lambda_function.zip 업로드 + 환경변수 설정
- Supabase: 테이블 생성

이제 S3 웹사이트에서 이름 입력 → Lambda API 호출 → Supabase 저장
