import requests
import json
import os

# 환경 변수에서 토큰 읽기
# 사용법: export NOTION_TOKEN="your_token_here" 후 실행
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
if not NOTION_TOKEN:
    raise ValueError("NOTION_TOKEN 환경 변수를 설정해주세요")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28"
}

# 검색
url = "https://api.notion.com/v1/search"
response = requests.post(url, headers=headers, json={"query": "CPA"})

# 상태 코드와 응답 확인
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
print(f"Response Headers: {dict(response.headers)}")

# JSON 파싱 시도
try:
    print("\nJSON Response:")
    print(json.dumps(response.json(), indent=2, ensure_ascii=False))
except:
    print("\nCannot parse as JSON")
