import os
import requests

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

# 원본 파일 경로 (한국어)
input_path = "docs/ko/index.md"
# 번역 결과 저장 경로 (영어)
output_path = "docs/en/index.md"

# 파일 읽기
with open(input_path, "r", encoding="utf-8") as f:
    source_text = f.read()

# 번역 요청
res = requests.post(
    DEEPL_API_URL,
    data={
        "auth_key": DEEPL_API_KEY,
        "text": source_text,
        "target_lang": "EN"
    }
)

translated = res.json()["translations"][0]["text"]

# 결과 저장
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(translated)
