# Higgsfield API로 이미지 한 장 만들기

Higgsfield 공식 Python SDK(`higgsfield-client`)로 텍스트 프롬프트에서 이미지 한 장을 생성하는 최소 예제입니다.

## 폴더 구성

```
higgs/
├── generate_image.py   # 이미지 생성 코드
├── prompts/prompt.txt  # 기본 프롬프트 (여기를 수정)
├── requirements.txt    # 필요한 라이브러리
├── .env.example        # API 키 입력 양식
└── .gitignore          # .env, outputs/ 는 깃허브에 올라가지 않음
```

---

## 1단계: API 키 발급받기

1. [Higgsfield Cloud](https://cloud.higgsfield.ai/)에 가입하고 로그인합니다.
2. API Keys 메뉴에서 새 키를 만들면 **API Key**와 **API Secret** 두 값이 나옵니다.
3. 두 값을 안전한 곳에 복사해 둡니다. (Secret은 다시 볼 수 없을 수 있어요)
4. 이미지 생성에는 크레딧이 사용되므로 잔액을 확인합니다.

## 2단계: 코드 내려받기

```bash
git clone https://github.com/00ooojj0507-dot/higgs.git
cd higgs
git checkout claude/huggingface-image-generation-hbb71p
```

## 3단계: Python 환경 준비 (Python 3.9 이상)

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

## 4단계: API 키 넣기

```bash
cp .env.example .env      # Windows: copy .env.example .env
```

`.env` 파일을 열어 1단계의 값으로 바꿉니다.

```
HF_API_KEY=발급받은-키
HF_API_SECRET=발급받은-시크릿
```

> ⚠️ `.env`는 `.gitignore`에 들어 있어 깃허브에 올라가지 않습니다. **키를 코드나 README에 직접 쓰지 마세요.**

## 5단계: 프롬프트 작성하기

`prompts/prompt.txt`를 원하는 내용으로 수정합니다. 영어로 쓰면 결과가 더 안정적입니다.

좋은 프롬프트 구조: **주제 + 장소/배경 + 조명 + 분위기 + 스타일/카메라**

```
A cozy small cafe on a rainy Seoul street at night,   ← 주제·장소
warm light glowing through the window,                 ← 조명
reflections on wet pavement,                           ← 디테일
cinematic, highly detailed, 35mm photo                 ← 스타일
```

다른 예시:
- `A cute orange cat astronaut floating in space, Earth in the background, soft studio lighting, 3D render, Pixar style`
- `Minimalist product photo of a white ceramic coffee mug on a beige table, soft morning sunlight, clean background`

## 6단계: 실행하기

```bash
python generate_image.py
```

또는 프롬프트를 바로 입력할 수도 있습니다.

```bash
python generate_image.py "a watercolor painting of Jeju island at sunrise"
```

성공하면 이미지 URL이 출력되고, 파일이 `outputs/` 폴더에 저장됩니다.

## 옵션 바꾸기

`generate_image.py`의 `arguments`에서 수정합니다.

| 항목 | 예시 값 | 설명 |
|------|---------|------|
| `resolution` | `"1K"`, `"2K"`, `"4K"` | 해상도 |
| `aspect_ratio` | `"1:1"`, `"16:9"`, `"9:16"`, `"4:3"` | 가로세로 비율 |

사용할 모델은 파일 상단의 `MODEL` 값입니다. 다른 모델 ID는 Higgsfield Cloud 문서에서 확인하세요.

## 7단계: 내 변경사항 깃허브에 올리기

프롬프트를 수정했다면 아래처럼 올립니다. (`.env`와 생성된 이미지는 자동으로 제외됩니다)

```bash
git add prompts/prompt.txt
git commit -m "Update prompt"
git push
```

## 자주 나는 오류

| 메시지 | 원인 / 해결 |
|--------|-------------|
| `CredentialsMissedError` | `.env` 파일이 없거나 키 이름이 틀림 → 4단계 확인 |
| `401` / `403` | 키 또는 시크릿 값이 잘못됨 → 다시 발급 |
| `402` / 크레딧 관련 | 크레딧 부족 → Higgsfield Cloud에서 충전 |
| `ModuleNotFoundError` | 가상환경 활성화 후 `pip install -r requirements.txt` |
