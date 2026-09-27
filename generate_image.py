"""Higgsfield API로 이미지 한 장을 생성해 outputs/ 폴더에 저장합니다.

사용법:
    python generate_image.py                      # prompts/prompt.txt 사용
    python generate_image.py "a cat astronaut"    # 프롬프트 직접 입력
"""
import sys
from datetime import datetime
from pathlib import Path

import higgsfield_client
import requests
from dotenv import load_dotenv

MODEL = "bytedance/seedream/v4/text-to-image"
PROMPT_FILE = Path("prompts/prompt.txt")
OUTPUT_DIR = Path("outputs")


def read_prompt() -> str:
    if len(sys.argv) > 1:
        return " ".join(sys.argv[1:])
    return PROMPT_FILE.read_text(encoding="utf-8").strip()


def main() -> None:
    load_dotenv()  # .env 의 HF_API_KEY / HF_API_SECRET 을 환경변수로 불러옴

    prompt = read_prompt()
    print(f"프롬프트: {prompt}")
    print("이미지 생성 요청 중... (수십 초 걸릴 수 있어요)")

    result = higgsfield_client.subscribe(
        MODEL,
        arguments={
            "prompt": prompt,
            "resolution": "2K",
            "aspect_ratio": "1:1",
        },
    )

    image_url = result["images"][0]["url"]
    print(f"생성 완료: {image_url}")

    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / f"image_{datetime.now():%Y%m%d_%H%M%S}.png"
    response = requests.get(image_url, timeout=60)
    response.raise_for_status()
    out_path.write_bytes(response.content)
    print(f"저장됨: {out_path}")


if __name__ == "__main__":
    main()
