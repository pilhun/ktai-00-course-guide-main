# 리스트는 값을 순서대로 모은 자료입니다. 대괄호 안에 쉼표로 구분합니다.
numbers = [10, 20, 30]
print("전체:", numbers)
# 첫 번째 위치는 1이 아니라 0입니다. len은 값의 개수를 알려 줍니다.
print("첫 번째 수:", numbers[0])
print("개수:", len(numbers))
# for는 목록의 값을 하나씩 number에 넣고 들여쓴 줄을 반복합니다.
for number in numbers:
    print("꺼낸 수:", number)
