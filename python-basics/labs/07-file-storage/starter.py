# 선택 파일 실습입니다. Path는 Python 기본 제공 파일 위치 기능입니다.
from pathlib import Path
message = "안녕하세요."  # TODO: 오늘 배운 내용을 한 문장으로 바꿉니다.
# 이 코드 파일 옆에 저장합니다. 다음 실행에서는 같은 파일의 내용을 덮어씁니다.
path = Path(__file__).with_name("practice-note.txt")
path.write_text(message, encoding="utf-8")
loaded = path.read_text(encoding="utf-8")  # 저장한 글자를 다시 읽습니다.
print("파일 내용:", loaded)
