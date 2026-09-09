import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = "gemini-3.7-flash"

url = (
    "https://generativelanguage.googleapis.com/"
    f"v1beta/models/{model}:generateContent"
)

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": api_key
}

payload = {
    "contents": [
        {
            "parts": [
                {
                    "text": "Responda apenas: Gemini funcionando."
                }
            ]
        }
    ]
}

response = requests.post(
    url,
    headers=headers,
    json=payload,
    timeout=60
)

print()
print("=" * 60)
print("TESTE DE CONEXÃO GEMINI")
print("=" * 60)

print()
print("HTTP STATUS:", response.status_code)

print()
print("RESPOSTA:")

print(response.text)

print()
print("=" * 60)