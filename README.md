# AI Git Commit & PR Generator

## 프로젝트 소개

Git 변경사항을 AI(Google Gemini)가 분석하여
Conventional Commit Message와
GitHub Pull Request Description을 자동 생성하는 CLI 프로그램입니다.

---

## 개발 환경

- Python 3.14
- Google Gemini API
- python-dotenv

---

## 설치

```bash
pip install -r requirements.txt
```

---

## 환경 변수

프로젝트 루트에 `.env` 파일을 생성합니다.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 실행

### Commit Message 생성

```bash
python3 main.py commit
```

### Pull Request 생성

```bash
python3 main.py pr
```

### Safe Mode

```bash
python3 main.py commit --safe-mode
```

---

## 프로젝트 구조

```
B6-2
│
├── main.py
├── ai_client.py
├── git_utils.py
├── masking.py
├── requirements.txt
├── .env
└── .gitignore
```

---

## 주요 기능

- Git Status 수집
- Git Diff 분석
- AI Commit Message 생성
- AI Pull Request 생성
- 환경변수(.env) 관리
- Safe Mode를 통한 민감정보 마스킹

---

## 사용 기술

- argparse
- subprocess
- python-dotenv
- Google Gemini API
- Regular Expression

---

## 예시

```
$ python3 main.py commit

feat(ai): implement commit message generation using Google Gemini
```

---

## 작성자

AI:SW Basic Assignment