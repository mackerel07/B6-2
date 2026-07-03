import os
from dotenv import load_dotenv
from google import genai
from masking import mask_sensitive_data

load_dotenv() #.env 파일 읽기

api_key = os.getenv("GEMINI_API_KEY") #환경변수 읽기

if api_key is None: #키가 없을때 오류처리
    raise ValueError("GEMINI_API_KEY가 설정되지 않았습니다.") #오류발생시키기

client = genai.Client(api_key=api_key) #Client 객체 생성


def generate_commit_message(
    status,
    diff,
    model,
    temperature,
    max_tokens
):


    prompt = f"""
    Git Status
    {status}

    Git Diff
    {diff}

    위 변경사항을 분석하여
    Conventional Commit 형식의
    커밋 메시지를 하나만 생성해.

    설명은 하지 말고
    커밋 메시지만 출력해.
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config={
            "temperature": temperature,
            "max_output_tokens": max_tokens
        }
    )

    return response.text

def generate_pr_message(
    status,
    diff,
    model,
    temperature,
    max_tokens
):

    prompt = f"""
    Git Status
    {status}

    Git Diff
    {diff}

    위 변경사항을 분석하여 GitHub Pull Request 설명을 작성해.

    다음 형식을 지켜.

    ## Summary
    (한 줄 요약)

    ## Changes
    - 변경사항1
    - 변경사항2
    - 변경사항3

    ## Test
    - 테스트 내용을 작성

    Markdown 형식으로만 출력해.
    """

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config={
            "temperature": temperature,
            "max_output_tokens": max_tokens
        }
    )

    return response.text

'''
GEMINI 연결
env 관리
test_connection
'''