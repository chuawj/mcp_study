import os
import requests
from dotenv import load_dotenv

# 환경변수에서 API 키 읽기
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

# Groq API 기본 설정
API_URL = "https://api.groq.com/openai/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# MCP 구조 메시지
messages = [
    {"role": "system", "content": "당신은 친절한 인공지능 비서입니다."},
    {"role": "user", "content": "MCP 구조에 대해 설명해줘."}
]

# 요청 본문
payload = {
    "model": "llama3-70b-8192",  # 또는 llama3-8b-8192
    "messages": messages,
    "temperature": 0.7
}

# API 호출
response = requests.post(API_URL, headers=HEADERS, json=payload)

# 응답 출력
if response.status_code == 200:
    answer = response.json()["choices"][0]["message"]["content"]
    print("🤖 LLM 응답:", answer)
else:
    print("❌ 오류 발생:", response.status_code, response.text)
