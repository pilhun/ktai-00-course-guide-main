# import는 다른 곳에 준비된 기능을 이 파일에서 사용할 수 있게 불러오는 문법입니다.
# json은 Python 설치 시 함께 제공되는 표준 라이브러리 모듈입니다. 별도 설치가 필요 없습니다.
# 여기서는 문의 딕셔너리·리스트를 JSON으로 바꾸거나 파일에서 다시 읽는 데 사용합니다.
# 모듈 전체를 불러왔으므로 아래에서 json.dump(), json.load()처럼 json.을 붙여 사용합니다.
import json
# from 모듈이름 import 기능이름은 모듈에서 필요한 이름을 골라 불러오는 문법입니다.
# pathlib는 파일·폴더의 위치를 다루는 Python 기본 제공 모듈이며 추가 설치가 필요 없습니다.
# 그 안의 Path는 파일 위치를 만들고 파일을 여는 기능을 가진 클래스입니다.
# Path를 직접 불러왔으므로 아래에서는 pathlib.Path 대신 Path(...)라고 적습니다.
# 예제의 Path(__file__).with_name(...)은 지금 실행하는 코드 파일 옆의 파일을 가리킵니다.
from pathlib import Path


MENU = """
1. 문의 추가
2. 전체 조회
3. 분류별 건수
4. 저장
5. 불러오기
q. 종료
"""


# 문의 본문에서 분류 기준을 검사합니다. 요금 조건을 먼저 확인해 두 기준에 모두 맞을 때 우선 적용합니다.
def classify_question(message):
    if "요금" in message:
        return "요금"
    if "계정" in message or "비밀번호" in message:
        return "계정"
    return "기타"


# 목록을 전달받아 유효한 문의만 추가합니다. 공백뿐인 입력이면 아래의 append()까지 진행하지 않습니다.
def add_question(questions):
    message = input("고객 문의> ").strip()
    if not message:
        print("문의를 입력해 주세요.")
        return

    # 삭제 기능이 없는 앱이므로 현재 건수를 이용해 다음 번호를 만들 수 있습니다.
    question = {
        "id": f"KT-{101 + len(questions)}",
        "message": message,
        "category": classify_question(message),
    }
    questions.append(question)
    print(f'{question["id"]} 접수 완료')


def show_questions(questions):
    if not questions:
        print("등록된 문의가 없습니다.")
        return

    for question in questions:
        print(f'{question["id"]} [{question["category"]}] {question["message"]}')


# 분류별 건수를 모두 0으로 시작한 다음 문의를 하나씩 읽으며 해당 분류의 건수만 늘립니다.
def show_summary(questions):
    counts = {"요금": 0, "계정": 0, "기타": 0}
    for question in questions:
        counts[question["category"]] += 1

    for category, count in counts.items():
        print(f"{category}: {count}건")
    print(f"전체: {len(questions)}건")


# w 모드는 연습 파일에 현재 목록을 다시 씁니다. UTF-8과 ensure_ascii=False를 써 한글을 읽기 쉽게 보관합니다.
def save_questions(questions, file_path):
    try:
        with file_path.open("w", encoding="utf-8") as file:
            json.dump(questions, file, ensure_ascii=False, indent=2)
    except OSError:
        print("파일을 저장할 수 없습니다.")
        return

    print(f"저장: {len(questions)}건")


# 파일이 없거나 형식이 잘못되면 None을 돌려줍니다. 정상적으로 읽은 빈 목록은 []입니다.
def load_questions(file_path):
    try:
        with file_path.open(encoding="utf-8") as file:
            questions = json.load(file)
    except FileNotFoundError:
        print("저장 파일이 없습니다.")
        return None
    except (OSError, UnicodeError, json.JSONDecodeError):
        print("저장 파일을 읽을 수 없습니다.")
        return None

    # 이 앱이 저장한 연속된 번호와 세 분류를 확인합니다.
    if not isinstance(questions, list):
        print("문의 목록 형식이 올바르지 않습니다.")
        return None

    for index, question in enumerate(questions, start=101):
        if (
            not isinstance(question, dict)
            or question.get("id") != f"KT-{index}"
            or not isinstance(question.get("message"), str)
            or not question["message"].strip()
            or question.get("category") not in ("요금", "계정", "기타")
        ):
            print("문의 목록 형식이 올바르지 않습니다.")
            return None

    print(f"불러오기: {len(questions)}건")
    return questions


# 메뉴 반복을 관리합니다. 파일 경로를 따로 받지 않으면 이 코드 옆의 연습 JSON을 사용합니다.
def main(file_path=None):
    if file_path is None:
        file_path = Path(__file__).with_name("practice-helpdesk.json")
    questions = []

    while True:
        print(MENU)
        choice = input("메뉴> ").strip().lower()

        if choice == "q":
            print("종료합니다.")
            break
        elif choice == "1":
            add_question(questions)
        elif choice == "2":
            show_questions(questions)
        elif choice == "3":
            show_summary(questions)
        elif choice == "4":
            save_questions(questions, file_path)
        elif choice == "5":
            loaded = load_questions(file_path)
            # 읽기 실패로 None을 받으면 현재 목록을 유지합니다. 빈 목록을 읽은 경우에는 현재 목록을 빈 목록으로 바꿉니다.
            if loaded is not None:
                questions = loaded
        else:
            print("메뉴 번호를 다시 확인하세요.")


# 파일을 직접 실행한 경우에만 메뉴를 시작합니다.
if __name__ == "__main__":
    main()
