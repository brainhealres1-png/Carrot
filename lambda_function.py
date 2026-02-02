import json
import urllib.request
import os

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))
        name = body.get("name", "").strip()
        
        if not name:
            return {"statusCode": 400, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps({"error": "이름을 입력해주세요."})}
        
        # Supabase에 저장
        url = f"{SUPABASE_URL}/rest/v1/names"
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json"
        }
        data = json.dumps({"name": name}).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        urllib.request.urlopen(req)
        
        return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps({"message": f"안녕하세요, {name}님! 👋"})}
    
    except Exception as e:
        return {"statusCode": 500, "headers": {"Access-Control-Allow-Origin": "*"}, "body": json.dumps({"error": str(e)})}
