card = int(input("카드 종류를 입력하세요 (1, 2, 3): "))

if card == 0:
    print("오류 입니다. 종료")
    exit()

if card == 1:
    print("캐쉬카드 입니다.")
elif card == 2:
    print("신용카드 입니다.")
elif card == 3:
    print("다른은행 카드 입니다.")
else:
    print("카드를 확인하세요.")

