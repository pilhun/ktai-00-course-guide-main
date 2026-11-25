# 선택 읽기 예제입니다. json은 Python 기본 모듈로 딕셔너리를 JSON 글자로 표현합니다.
# JSON은 다른 프로그램과 자료를 주고받을 때 쓰는 텍스트 형식입니다. 추가 설치는 없습니다.
import json
student = {"name": "민지", "age": 20}
# ensure_ascii=False는 한글이 눈에 보이게 출력하는 설정입니다. 먼저 준비된 상태로 사용합니다.
text = json.dumps(student, ensure_ascii=False)
print("JSON:", text)
