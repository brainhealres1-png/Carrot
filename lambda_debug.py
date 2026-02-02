import json
import urllib.request
import os

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

def lambda_handler(event, context):
    try:
        print("=== Lambda 시작 ===")
        print(f"Event: {event}")
        
        # body 파싱
        print("1. Body 파싱 시작")
        if isinstance(event.get("body"), str):
            print("   - Body는 문자열")
            body = json.loads(event.get("body", "{}"))
        else:
            print("   - Body는 문자열 아님")
            body = event.get("body", {})
        
        print(f"2. Parsed body: {body}")
        
        name = body.get("name", "").strip() if body else ""
        print(f"3. Name: {name}")
        
        if not name:
            print("4. 이름이 없음 - 에러 반환")
            return {"statusCode": 400, "headers": {"Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}, "body": json.dumps({"error": "이름을 입력해주세요."})}
        
        print(f"5. Supabase URL: {SUPABASE_URL}")
        url = f"{SUPABASE_URL}/rest/v1/names"
        print(f"6. 요청 URL: {url}")
        
        headers = {"apikey": SUPABASE_KEY, "Authorization": f"Bearer {SUPABASE_KEY}", "Content-Type": "application/json"}
        print(f"7. Headers 설정 완료")
        
        data = json.dumps({"name": name}).encode('utf-8')
        print(f"8. Data: {data}")
        
        req = urllib.request.Request(url, data=data, headers=headers, method='POST')
        print(f"9. Request 생성 완료")
        
        response = urllib.request.urlopen(req)
        print(f"10. Supabase 응답: {response.status}")
        
        print("=== Lambda 성공 ===")
        return {"statusCode": 200, "headers": {"Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}, "body": json.dumps({"message": f"안녕하세요, {name}님! 👋"})}
    
    except Exception as e:
        print(f"=== Lambda 오류 ===")
        print(f"오류: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return {"statusCode": 500, "headers": {"Access-Control-Allow-Origin": "*", "Content-Type": "application/json"}, "body": json.dumps({"error": str(e)})}
