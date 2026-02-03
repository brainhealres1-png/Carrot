import json
import urllib.request
import os

# Lambda 환경 변수에서 Supabase URL / Key 가져오기
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

def lambda_handler(event, context):
    # 모든 응답에 공통 CORS 헤더
    cors_headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Content-Type": "application/json"
    }

    # OPTIONS 요청 처리 (preflight)
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": ""
        }

    try:
        # POST body 처리
        body = event.get("body")
        if body:
            if isinstance(body, str):
                body = json.loads(body)
        else:
            body = {}

        # GET query 처리
        query = event.get("queryStringParameters") or {}

        # name 값 우선순위: POST body > GET query
        name = (body.get("name") if body.get("name") else query.get("name", "")).strip()

        if not name:
            return {
                "statusCode": 400,
                "headers": cors_headers,
                "body": json.dumps({"error": "이름을 입력해주세요."})
            }

        # Supabase 요청
        url = f"{SUPABASE_URL}/rest/v1/names"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        }
        data = json.dumps({"name": name}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers=headers, method="POST")

        # Supabase 호출
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        if status_code not in (200, 201):
            raise Exception(f"Supabase 저장 실패, status code: {status_code}")

        # 정상 응답
        return {
            "statusCode": 200,
            "headers": cors_headers,
            "body": json.dumps({"message": f"안녕하세요, {name}님! 👋"})
        }

    except Exception as e:
        # CloudWatch 로그에도 에러 출력
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "headers": cors_headers,
            "body": json.dumps({"error": str(e)})
        }
