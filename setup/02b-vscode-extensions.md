# VS Code 확장 설치와 교안 보기

[← 설치와 첫 실행](README.md)

확장은 VS Code에 기능을 더하는 프로그램입니다. 처음에는 Python을 실행할 준비를 하고, Markdown 교안을 미리 보기로 읽습니다.

| 항목 | 준비 방법 | 사용하는 곳 |
|---|---|---|
| Python · Microsoft | 이 페이지를 따라 설치합니다. | .py 파일 실행과 Python 환경 선택 |
| Markdown 미리 보기 | VS Code 기본 기능을 사용합니다. | README.md의 표·그림·흐름도 읽기 |
| Markdown All in One | 문서를 직접 작성할 때 선택해 설치합니다. | 목록과 목차 등 Markdown 편집 |
| Pylance 등 Python 보조 확장 | Python 설치 시 함께 준비되는 항목을 확인합니다. | 코드 자동완성과 오류 표시 |

Copilot은 04부터 필요할 때 참고하고 Codex 앱은 07부터 선택적으로 사용합니다. Docker Desktop은 사용하는 교과에서 준비합니다.

VS Code의 Git 기능은 기본 내장 기능입니다. 수업 자료와 실습 파일은 [자료 받기와 업로드](04-git-github.md)에서 안내하는 브라우저 버튼으로 주고받습니다.

## 확장 화면에서 설치하기

1. VS Code 왼쪽의 블록 모양 **Extensions(확장)** 아이콘을 누릅니다.
2. 검색창에 `@id:ms-python.python`을 붙여 넣습니다.
3. 이름이 **Python**, 게시자가 **Microsoft**인 항목을 선택합니다.
4. **Install(설치)**을 누르고 완료될 때까지 기다립니다.
5. 버튼이 **Uninstall(제거)** 또는 톱니바퀴로 바뀌면 설치된 상태입니다. Reload가 표시되면 눌러 다시 엽니다.

설치가 완료되면 다음 단계로 진행합니다.

[Python 확장 공식 페이지](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

## Python 인터프리터 선택

[첫 Python 실행](../python-basics/01-run-and-print/README.md)에서는 먼저 파일을 열고 ▶를 누릅니다. 인사말이 정상 출력되면 다음 실습으로 진행합니다.

Python을 선택하라는 안내가 나오거나 실행이 안 될 때 아래를 확인합니다. 인터프리터는 코드를 실행하는 Python 프로그램입니다.

1. 선택 안내가 나오면 목록에서 **Python 3.12.10**을 고릅니다. 표시가 Python 3.12로만 보이면 설치 안내의 버전 확인 방법을 참고합니다.
2. 선택 화면을 직접 열어야 한다면 **View → Command Palette**에서 `Python: Select Interpreter`를 검색합니다.
3. 목록이 비어 있으면 [Python 설치](01-python-install.md)를 마쳤는지 확인하고 VS Code를 완전히 종료했다 다시 엽니다.
4. 같은 파일에서 ▶를 다시 눌러 실행 결과를 확인합니다.

## README.md를 교재처럼 보기

1. [수업 자료 받기](04-git-github.md)를 마친 뒤 VS Code 왼쪽에서 README.md를 클릭합니다.
2. **View → Command Palette(보기 → 명령 팔레트)**를 엽니다.
3. `Markdown: Open Preview to the Side`를 검색해 선택합니다.
4. 오른쪽에 제목, 표, 그림이 정리된 교안이 열립니다. 왼쪽은 원문, 오른쪽은 읽기 화면입니다.
5. 오른쪽의 링크를 눌러 다음 안내를 엽니다. 새 문서가 원문으로 열리면 같은 미리 보기 메뉴를 사용합니다.

Windows는 `Ctrl+Shift+V`, macOS는 `Cmd+Shift+V`로 미리 보기를 열 수도 있습니다. 파일 이름 끝이 .md인지 먼저 확인합니다.

### 흐름도가 글자로 보일 때

최신 VS Code에서는 Mermaid 흐름도를 기본 미리 보기로 표시합니다. 원문의 `flowchart`가 보인다면 먼저 미리 보기 화면을 열었는지 확인합니다. 오래된 버전에서 그림이 나오지 않으면 VS Code를 업데이트하고 다시 엽니다.

Markdown Preview Mermaid Support의 기능은 VS Code에 통합되어 있습니다. 교안은 기본 미리 보기로 읽습니다.

[Microsoft Markdown 안내](https://code.visualstudio.com/docs/languages/markdown) · [Mermaid 확장의 기능 통합 안내](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

## 선택 · Markdown All in One 설치

README를 직접 작성하는 활동에서 설치할 수 있습니다.

1. 왼쪽 Extensions를 엽니다.
2. `@id:yzhang.markdown-all-in-one`을 검색합니다.
3. **Markdown All in One**, 게시자 **Yu Zhang**을 확인하고 Install을 누릅니다.
4. README를 열어 목록 작성과 편집에 사용합니다.

[Markdown All in One 공식 확장 페이지](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

## 준비 완료 확인

- [ ] Microsoft Python 확장이 설치됐습니다.
- [ ] 수업 폴더의 Python 예제를 ▶로 실행했습니다.
- [ ] README.md를 미리 보기로 열어 표와 흐름도를 확인했습니다.

[Microsoft 확장 설치 안내](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace)

[다음 · 수업 자료 받기](04-git-github.md) · [자료가 준비됐다면 첫 실행](../python-basics/01-run-and-print/README.md)
