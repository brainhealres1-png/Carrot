import json
import os
from supabase import create_client, Client

# 환경변수에서 Supabase 정보 읽기
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL과 SUPABASE_KEY 환경변수가 필요합니다")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def lambda_handler(event, context):
    """
    Lambda 핸들러 - 이름을 Supabase에 저장
    """
    try:
        # POST 요청 처리
        if event.get("httpMethod") == "POST":
            body = json.loads(event.get("body", "{}"))
            name = body.get("name", "").strip()
            
            if not name:
                return {
                    "statusCode": 400,
                    "headers": {
                        "Content-Type": "application/json",
                        "Access-Control-Allow-Origin": "*"
                    },
                    "body": json.dumps({"error": "이름을 입력해주세요."})
                }
            
            # Supabase에 저장
            response = supabase.table("names").insert({
                "name": name
            }).execute()
            
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({
                    "success": True,
                    "message": f"안녕하세요, {name}님! 👋"
                })
            }
        
        # GET 요청 - 모든 이름 조회
        elif event.get("httpMethod") == "GET":
            response = supabase.table("names").select("*").execute()
            
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": json.dumps({
                    "success": True,
                    "data": response.data
                })
            }
        
        # OPTIONS 요청 (CORS)
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
            return {
                "statusCode": 405,
                "body": json.dumps({"error": "Method not allowed"})
            }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }
