# import는 다른 곳에 준비된 기능을 이 파일에서 사용할 수 있게 불러오는 문법입니다.
# json은 Python 설치 시 함께 제공되는 표준 라이브러리 모듈입니다. 별도 설치가 필요 없습니다.
# 여기서는 문의 딕셔너리·리스트를 JSON으로 바꾸거나 파일에서 다시 읽는 데 사용합니다.
# 모듈 전체를 불러왔으므로 아래에서 json.dump(), json.load()처럼 json.을 붙여 사용합니다.
import json


# 문의 내용을 받아 번호와 본문이 든 딕셔너리를 반환합니다.
def make_question(message):
    return {"id": "KT-101", "message": message}


# 입력을 받고 공백을 정리한 다음에 유효 여부를 판단합니다.
message = input("고객 문의를 입력하세요> ").strip()
# 문자열이 비어 있지 않을 때만 함수를 호출하고 JSON을 화면에 출력합니다.
if message:
    question = make_question(message)
    print(json.dumps(question, ensure_ascii=False, indent=2))
# 빈 문의는 접수하지 않고 안내 문구만 표시합니다.
else:
    print("문의를 입력해 주세요.")
