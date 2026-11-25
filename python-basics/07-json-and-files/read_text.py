# from ... import ...는 다른 곳의 기능을 가져오는 문법입니다.
# pathlib는 Python 기본 제공 모듈이고 Path는 파일 위치를 다루는 기능입니다. 추가 설치는 없습니다.
from pathlib import Path
# __file__은 지금 실행한 Python 파일의 위치입니다. 옆에 있는 greeting.txt를 찾는 준비 코드입니다.
path = Path(__file__).with_name("greeting.txt")
# read_text는 파일의 글자를 읽습니다. UTF-8은 한글을 읽고 쓰는 문자 저장 방식입니다.
message = path.read_text(encoding="utf-8")
print("읽은 내용:", message)
