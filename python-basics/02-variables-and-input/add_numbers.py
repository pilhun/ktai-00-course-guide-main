# input의 결과는 글자입니다. 먼저 두 값을 입력받아 각각 보관합니다.
first_text = input("첫 번째 정수> ")
second_text = input("두 번째 정수> ")
# int는 숫자 형태의 글자를 정수로 바꿉니다. 예: "3"을 정수 3으로 바꿉니다.
first = int(first_text)
second = int(second_text)
# 정수로 바꾼 뒤 더합니다. 문자열 "3" + "5"의 결과 "35"와 구분합니다.
total = first + second
print("합계:", total)
# 처음에는 3, 5처럼 정수만 입력합니다. 잘못된 입력의 오류는 선택 랩에서 봅니다.
