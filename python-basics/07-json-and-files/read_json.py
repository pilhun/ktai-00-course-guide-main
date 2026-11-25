# 선택 읽기 예제입니다. json과 pathlib는 모두 Python에 포함된 기본 모듈입니다.
import json
from pathlib import Path
# 예제 JSON 파일은 Python처럼 실행하는 파일이 아니라 읽을 자료입니다.
path = Path(__file__).with_name("sample_student.json")
text = path.read_text(encoding="utf-8")
student = json.loads(text)  # JSON 글자를 Python 딕셔너리로 바꾸는 준비 코드입니다.
print("이름:", student["name"])
print("나이:", student["age"])
