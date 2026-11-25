# 준비 중 막혔을 때

먼저 **어디까지 성공했는지** 찾습니다. 예를 들어 Python 버전은 나오는데 파일이 없다는 오류가 뜨면 Python이 이미 실행된 상태입니다. 그때는 현재 폴더와 실행할 파일 경로를 확인합니다.

| 증상 | 확인할 것 |
|---|---|
| ▶ 실행 버튼이 안 보임 | .py 파일을 열었는지와 [Python 확장](../setup/02b-vscode-extensions.md) 설치를 확인합니다. |
| 화면 아래에 질문만 나오고 멈춘 것 같음 | Terminal을 클릭해 답을 입력하고 Enter를 누릅니다. |
| 고친 문구가 출력되지 않음 | Auto Save가 켜져 있는지 확인합니다. 아직 저장되지 않았다면 File → Save를 누르고 같은 파일의 ▶로 다시 실행합니다. |
| ZIP 안에서 파일을 보고 있음 | [압축 풀기와 자료 복사](../setup/04-git-github.md)를 마친 뒤 교과 폴더를 엽니다. |
| Windows의 `py` 또는 macOS의 `python3`를 찾을 수 없음 | 새 터미널을 열고 [설치 확인](../setup/01-python-install.md)을 반복합니다. |
| Python 파일이 없다는 오류 | 터미널의 [현재 폴더](../setup/03-terminal-basics.md)와 README 위치가 맞는지 확인합니다. |
| VS Code가 다른 버전을 실행함 | [인터프리터 선택](../setup/02b-vscode-extensions.md#python-인터프리터-선택)을 다시 확인합니다. |
| VS Code에서 GitHub 연결이 안 됨 | [GitHub 계정의 이메일 확인](../setup/00-github-account.md)을 마쳤는지 확인하고, [VS Code 로그인 안내](../setup/02a-vscode-github-login.md)에서 브라우저 인증을 완료합니다. |
| GitHub에서 저장소를 찾을 수 없음 | 주소와 로그인 계정, 비공개 저장소 초대 여부를 확인합니다. |
| Codex가 열리지 않음 | Codex 설치를 진행한 교과에서 앱 설치와 로그인을 확인한 뒤 07 교과의 ai-coding 안내를 참고합니다. |
| Copilot Chat이나 자동완성이 멈춤 | 04 교과 ai-coding 폴더의 Copilot 사용 한도 안내에서 로그인한 GitHub 계정과 각 기능의 남은 사용량을 확인합니다. |

선생님에게 도움을 요청할 때는 운영체제, 열어 둔 파일 이름, 누른 버튼 또는 입력한 명령, 오류 메시지 마지막 줄을 적어 주세요. 키나 비밀번호가 보이면 먼저 가립니다.

## 도움 요청 예시

```text
활동: 공통 가이드 첫 Python 실행
운영체제: Windows / PowerShell
열어 둔 파일: python-basics/01-run-and-print/print_examples.py
한 동작: 오른쪽 위 ▶의 Run Python File in Terminal
오류 마지막 줄: No such file or directory
```

이 예시라면 [현재 폴더 확인](../setup/03-terminal-basics.md)에서 탐색기와 터미널의 위치가 일치하는지부터 점검합니다.

## 오류를 보고 다음 행동 정하기

| 마지막에 보이는 문구 | 뜻과 확인할 것 |
|---|---|
| `can't open file` | Python은 실행됐고 파일을 못 찾았습니다. [현재 폴더와 명령](../setup/03-terminal-basics.md)을 비교합니다. |
| `SyntaxError` 또는 `IndentationError` | 오류가 지목한 줄과 그 위 줄에서 따옴표, 괄호, 콜론, 들여쓰기를 봅니다. |
| `KeyError` | 딕셔너리에 없는 이름을 찾았습니다. [키 이름](../python-basics/05-dictionaries/README.md)을 대조합니다. |
| `ModuleNotFoundError` | 00 기본 예제의 import 철자와 실행 파일이 맞는지 확인합니다. 외부 라이브러리를 사용하는 01 이후 예제라면 해당 교과 SETUP.md를 따릅니다. |

오류를 고쳤다면 파일을 저장하고 같은 ▶ 버튼 또는 명령으로 다시 실행합니다. 오류가 사라졌더라도 예상한 출력까지 나오는지 확인하세요.
