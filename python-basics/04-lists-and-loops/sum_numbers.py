# 합계는 0부터 시작해서 수를 하나씩 더합니다.
total = 0
# range(1, 6)은 1부터 5까지 만듭니다. 끝값 6은 포함하지 않습니다.
for number in range(1, 6):
    total = total + number  # 이전 합계에 이번 수를 더해 새 합계를 저장합니다.
print("1부터 5까지 합계:", total)
