# CORS 에러 해결 가이드

## 문제
- CORS 정책으로 인해 S3 프론트엔드에서 Lambda API 호출 실패
- 502 Bad Gateway 에러 발생

## 원인
API Gateway에서 CORS 설정이 제대로 되어있지 않음. Lambda 함수에 CORS 헤더가 있어도 API Gateway 레벨에서 차단됨.

## 해결 방법

### 방법 1: AWS Console에서 CORS 설정 (권장)

1. **AWS API Gateway 콘솔 접속**
   - https://console.aws.amazon.com/apigateway

2. **API 선택**
   - 현재 사용 중인 API 선택 (wjefslt175)

3. **리소스 선택**
   - `/carrot` 리소스 선택

4. **CORS 활성화**
   - 리소스 우클릭 → "Enable CORS and replace existing CORS headers"
   - 또는 Actions → "Enable CORS and replace existing CORS headers"

5. **설정값**
   - Access-Control-Allow-Headers: `Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token`
   - Access-Control-Allow-Origin: `*` (또는 특정 도메인)

6. **배포**
   - Actions → Deploy API
   - Stage: `prod` 선택
   - Deploy 클릭

### 방법 2: CloudFormation/SAM으로 설정

Lambda 함수 앞에 API Gateway를 정의할 때:

```yaml
Resources:
  CarrotApi:
    Type: AWS::ApiGateway::RestApi
    Properties:
      Name: carrot-api
      
  CarrotResource:
    Type: AWS::ApiGateway::Resource
    Properties:
      RestApiId: !Ref CarrotApi
      ParentId: !GetAtt CarrotApi.RootResourceId
      PathPart: carrot
      
  CarrotMethod:
    Type: AWS::ApiGateway::Method
    Properties:
      RestApiId: !Ref CarrotApi
      ResourceId: !Ref CarrotResource
      HttpMethod: POST
      AuthorizationType: NONE
      Integration:
        Type: AWS_PROXY
        IntegrationHttpMethod: POST
        Uri: !Sub arn:aws:apigateway:${AWS::Region}:lambda:path/2015-03-31/functions/${CarrotFunction.Arn}/invocations
```

### 방법 3: 빠른 테스트 (Lambda 함수 수정)

현재 Lambda 함수의 CORS 헤더는 올바르지만, 다음과 같이 수정하면 더 안정적:

```python
def lambda_handler(event, context):
    cors_headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Content-Type": "application/json"
    }
    
    # ... 나머지 코드
```

## 확인 방법

1. **브라우저 개발자 도구 (F12) → Network 탭**
   - 요청 클릭
   - Response Headers 확인
   - `Access-Control-Allow-Origin` 헤더 존재 확인

2. **curl 테스트**
```bash
curl -X OPTIONS https://wjefslt175.execute-api.ap-northeast-2.amazonaws.com/prod/carrot \
  -H "Origin: http://aaaabbbbaaababaa.s3-website.ap-northeast-2.amazonaws.com" \
  -H "Access-Control-Request-Method: POST" \
  -v
```

## 추가 확인사항

- [ ] API Gateway 배포 완료 여부
- [ ] Lambda 함수 권한 확인 (API Gateway 호출 권한)
- [ ] 환경 변수 (SUPABASE_URL, SUPABASE_KEY) 설정 확인
- [ ] S3 버킷 정책에서 CloudFront/API Gateway 접근 허용 확인

## 참고
- AWS API Gateway CORS 공식 문서: https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-cors.html
