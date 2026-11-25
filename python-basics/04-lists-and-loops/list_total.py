# 리스트에 있는 숫자 세 개의 합계와 평균을 구합니다.
numbers = [10, 20, 30]
total = 0  # 합계는 0에서 시작합니다.
for number in numbers:  # 각 수를 하나씩 꺼냅니다.
    total = total + number
# len은 목록에 들어 있는 값의 개수입니다. 이 예제의 목록에는 세 수가 있습니다.
average = total / len(numbers)
print("합계:", total)
print("평균:", average)
# 처음에는 숫자 한 개만 바꿉니다. 빈 목록은 나눌 개수가 0이라 이 예제의 입력 조건이 아닙니다.
