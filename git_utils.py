import subprocess

def get_git_status():
    result = subprocess.run( #명령어 실행
        ["git", "status", "--short"], #subprocess를 통해서 리스트형태로 입력
        capture_output=True, #arg에 저장(python3 arg)
        text=True #str 변환
    )

    return result.stdout #명령어 출력

def get_git_diff():
    result = subprocess.run(
        ["git", "diff"],
        capture_output=True,
        text=True
    )

    return result.stdout

# python main.py commit> git status 실행> git diff 실행> 결과를 문자열로 저장


