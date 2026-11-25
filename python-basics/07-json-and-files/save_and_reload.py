# pathlib의 Path는 Python에 포함된 파일 위치 기능입니다. pip 설치는 하지 않습니다.
from pathlib import Path
message = "오늘도 Python을 연습합니다."  # 학생은 먼저 저장할 문장 한 곳을 바꿉니다.
# 지금 코드와 같은 폴더에 파일을 만듭니다. 기존 같은 이름 파일이 있으면 내용을 바꿉니다.
path = Path(__file__).with_name("practice-note.txt")
path.write_text(message, encoding="utf-8")
# 방금 쓴 파일을 다시 읽고 화면으로 확인합니다.
loaded = path.read_text(encoding="utf-8")
print("다시 읽은 내용:", loaded)
