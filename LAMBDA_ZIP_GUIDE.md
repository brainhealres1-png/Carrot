# Lambda ZIP 파일 생성 가이드

## ZIP 파일에 포함될 파일

```
lambda_function.zip
├── lambda_handler.py          ← Lambda 함수 코드
├── supabase/                  ← 의존성 (자동 설치)
├── python_dotenv/             ← 의존성 (자동 설치)
└── (기타 의존성 폴더들)
```

---

## 단계별 생성 방법

### 1. 임시 폴더 생성
```powershell
mkdir lambda_deploy
cd lambda_deploy
```

### 2. 의존성 설치
```powershell
pip install -r ..\lambda_requirements.txt -t .
```

이 명령어는 `lambda_requirements.txt`에 있는 패키지들을 현재 폴더에 설치합니다.

### 3. lambda_handler.py 복사
```powershell
copy ..\lambda_handler.py .
```

### 4. ZIP 파일 생성
```powershell
Compress-Archive -Path * -DestinationPath lambda_function.zip
```

### 5. 확인
```powershell
# ZIP 파일 내용 확인
Expand-Archive -Path lambda_function.zip -DestinationPath test_extract
Get-ChildItem -Path test_extract -Recurse
```

---

## 최종 ZIP 파일 구조

```
lambda_function.zip
├── lambda_handler.py
├── supabase/
│   ├── __init__.py
│   ├── client.py
│   └── ...
├── dotenv/
│   ├── __init__.py
│   └── ...
└── (기타 의존성)
```

---

## AWS Lambda 콘솔에서 업로드

1. AWS Lambda 콘솔 열기
2. 함수명: `carrot-api` 선택
3. Code 탭 → Upload from → .zip file
4. `lambda_function.zip` 선택 후 업로드
5. 핸들러 설정: `lambda_handler.lambda_handler`

---

## lambda_requirements.txt 내용

```
supabase==2.4.0
python-dotenv==1.0.0
```

---

## 주의사항

⚠️ ZIP 파일에 포함되면 안 되는 것:
- `.env` 파일 (환경변수로 설정)
- `__pycache__` 폴더
- `.git` 폴더
- 기타 불필요한 파일

✓ 반드시 포함되어야 하는 것:
- `lambda_handler.py`
- 모든 의존성 패키지
