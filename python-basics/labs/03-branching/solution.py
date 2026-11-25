# 직접 시도한 뒤 비교하는 풀이입니다. 바뀐 한 줄과 출력 결과를 확인합니다.
number = int(input("정수> "))  # 3, 0, -2를 차례로 입력해 봅니다.
# 풀이: False 대신 number가 0보다 큰지 비교하는 조건을 넣습니다.
if number > 0:
    print("양수입니다.")
elif number == 0:  # ==는 두 값이 같은지 비교합니다.
    print("0입니다.")
else:
    print("음수입니다.")
