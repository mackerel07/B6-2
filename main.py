from masking import mask_sensitive_data
import argparse #CLI 표준 라이브러리
from git_utils import get_git_status, get_git_diff
from ai_client import (generate_commit_message, generate_pr_message)

def main():
    parser = argparse.ArgumentParser( #CLI 분석객체
        description="AI 기반 Git Commit & PR 생성기"
    )

    parser.add_argument( #커맨드 추가
        "command",
        choices=["commit", "pr"], #둘 중 하나만
        help="실행할 명령(commit 또는 pr)"
    )

    parser.add_argument(
        "--model",
        default="gpt-4.1-mini",
        help="AI 모델"
    )

    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="Temperature"
    )

    parser.add_argument(
        "--max-tokens",
        type=int,
        default=700,
        help="최대 토큰 수"
    )

    parser.add_argument(
        "--safe-mode",
        action="store_true",
        help="민감정보 마스킹 활성화"
    )

    args = parser.parse_args() #인자분석 완료, 입력한 커맨드 읽기 (위치가 중요함)

    status = get_git_status() #변경사항이 없으면 종료

    if status.strip() == "":
        print("[INFO] 변경 사항이 없습니다.")
        return

    diff = get_git_diff() #git diff 결과 저장

    if args.safe_mode:
        diff = mask_sensitive_data(diff)

    if args.command == "commit":
        print("Commit 명령 실행")
        message = generate_commit_message(status, diff)
        print("\n=== AI Commit Message ===")
        print(message)

    elif args.command == "pr":
        print("PR 명령 실행")
        message = generate_pr_message(status, diff)
        print("\n=== AI PR Description ===")
        print(message)

if __name__ == "__main__":
    main()

'''
python main.py commit
parser 객체: python>main.py>commit으로 분리
args.command > commit
'''