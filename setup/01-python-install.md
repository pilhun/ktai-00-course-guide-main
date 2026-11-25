# Python 3.12.10 설치

[← 설치와 첫 실행](README.md)

Python은 우리가 만든 코드를 실행하는 프로그램입니다. **이 수업의 설치 기준 버전은 Python 3.12.10입니다.** 아래에서 내 컴퓨터의 운영체제 부분을 따라갑니다. 다른 버전을 고르지 않도록 연결된 3.12.10 전용 다운로드 페이지를 사용합니다.

## Windows에서 설치하기

1. [Python 3.12.10 다운로드 페이지](https://www.python.org/downloads/release/python-31210/)를 엽니다.
2. 아래쪽 **Files**에서 일반적인 Intel·AMD Windows PC는 **Windows installer (64-bit)**를 선택합니다. ARM 기반 PC라면 선생님에게 기기 종류를 알려 설치 파일을 확인합니다.
3. 다운로드한 설치 파일을 두 번 클릭합니다.
4. 첫 화면 아래에 **Add python.exe to PATH**가 보이면 체크합니다.
5. **Install Now**를 누릅니다. 컴퓨터 변경 허용 창이 뜨면 설치 파일을 확인하고 진행합니다.
6. **Setup was successful**이 나오면 Close를 누릅니다.
7. 이미 설치되어 Modify·Repair 등의 화면이 보이면 창을 닫고 아래 첫 실행 준비 단계로 진행합니다.

Windows와 macOS 모두 **Python 3.12.10**으로 맞춥니다. 이미 다른 버전이 있다면 기존 프로그램을 바로 삭제하지 말고 선생님과 사용할 버전을 확인합니다.

## macOS에서 설치하기

1. [Python 3.12.10 다운로드 페이지](https://www.python.org/downloads/release/python-31210/)의 Files에서 **macOS 64-bit universal2 installer**를 누릅니다. Apple Silicon과 Intel을 지원합니다.
2. 다운로드한 `.pkg` 파일을 두 번 클릭합니다.
3. **계속 → 사용권 계약 확인 → 설치** 순서로 진행합니다. Mac 암호를 요청하면 입력합니다.
4. 설치 성공 화면을 확인하고 닫습니다.
5. Finder의 **응용 프로그램 → Python 3.12** 안에 `Install Certificates.command`가 있으면 두 번 클릭해 인증서를 준비합니다. 실행이 끝나면 그 창을 닫습니다.

## 버전을 확인하고 싶다면 · 선택

Windows PowerShell에서는 `py --version`, macOS 터미널에서는 `python3 --version`을 실행합니다. 수업 기준 출력은 `Python 3.12.10`입니다. 다른 버전이 나오면 선생님에게 출력 내용을 알려 주세요.

실행 명령에 버전 번호를 붙이지 않습니다. Windows는 `py`, macOS는 `python3`로 실행합니다. Mac의 응용 프로그램 폴더 이름은 Python 3.12로 표시될 수 있습니다.

## 설치 후 첫 실행 준비

VS Code를 열어 두었다면 완전히 종료했다 다시 엽니다. 이어서 [Python 확장 설치](02b-vscode-extensions.md)를 진행합니다. 수업 자료를 열어 ▶로 실행합니다. Python을 찾지 못할 때는 해당 문서의 문제 해결 안내를 확인합니다.

**완료 확인** — 설치 성공 화면을 확인했습니다. 최종 동작 확인은 [첫 Python 실행](../python-basics/01-run-and-print/README.md)에서 인사말을 출력하며 진행합니다.

[Python Windows 공식 안내](https://docs.python.org/3.12/using/windows.html) · [macOS 공식 안내](https://docs.python.org/3.12/using/mac.html)

[다음 · Python 확장 설치](02b-vscode-extensions.md)
