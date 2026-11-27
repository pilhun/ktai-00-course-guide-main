# 1부터 100까지 숫자 중 랜덤하게 10개를 뽑아 리스트에 담습니다.
# 10개의 숫자를 출력한다.

import random

num_list = list(range(1, 101))

pick_list = random.sample(num_list, 10)

for num in pick_list:
    print(num)

# 10개의 숫자 중 3의 배수만 출력한다.

three_sum = 0
three_count = 0

for num in pick_list:
    if num % 3 == 0:
        print("3의 배수 :", num)
        three_sum = three_sum + num
        three_count = three_count + 1

# 3의 배수의 합과 평균을 구하시오.

if three_count == 0:
    print("3의 배수가 없습니다.")
else:
    three_average = three_sum / three_count
    print("3의 배수의 합 :", three_sum)
    print("3의 배수의 평균 :", three_average)


