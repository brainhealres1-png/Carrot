import json
import os
import urllib.request
import urllib.error

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

def lambda_handler(event, context):
    """
    경량화된 Lambda 핸들러 - Supabase REST API 사용
    """
    try:
        if event.get("httpMethod") == "POST":
            body = json.loads(event.get("body", "{}"))
            name = body.get("name", "").strip()
            
            if not name:
                return {
                    "statusCode": 400,
                    "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                    "body": json.dumps({"error": "이름을 입력해주세요."})
                }
            
            # Supabase REST API로 데이터 저장
            url = f"{SUPABASE_URL}/rest/v1/names"
            headers = {
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}",
                "Content-Type": "application/json"
            }
            data = json.dumps({"name": name}).encode('utf-8')
            
            req = urllib.request.Request(url, data=data, headers=headers, method='POST')
            
            try:
                with urllib.request.urlopen(req) as response:
                    return {
                        "statusCode": 200,
                        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                        "body": json.dumps({"success": True, "message": f"안녕하세요, {name}님! 👋"})
                    }
            except urllib.error.HTTPError as e:
                return {
                    "statusCode": 500,
                    "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                    "body": json.dumps({"error": f"DB 저장 실패: {e.reason}"})
                }
        
        elif event.get("httpMethod") == "GET":
            url = f"{SUPABASE_URL}/rest/v1/names"
            headers = {
                "apikey": SUPABASE_KEY,
                "Authorization": f"Bearer {SUPABASE_KEY}"
            }
            
            req = urllib.request.Request(url, headers=headers)
            
            try:
                with urllib.request.urlopen(req) as response:
                    data = json.loads(response.read().decode('utf-8'))
                    return {
                        "statusCode": 200,
                        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                        "body": json.dumps({"success": True, "data": data})
                    }
            except urllib.error.HTTPError as e:
                return {
                    "statusCode": 500,
                    "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
                    "body": json.dumps({"error": str(e)})
                }
        
        elif event.get("httpMethod") == "OPTIONS":
            return {
                "statusCode": 200,
                "headers": {
                    "Access-Control-Allow-Origin": "*",
                    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                    "Access-Control-Allow-Headers": "Content-Type"
                }
            }
        
        else:
            return {"statusCode": 405, "body": json.dumps({"error": "Method not allowed"})}
    
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
