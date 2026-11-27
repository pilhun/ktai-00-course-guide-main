num_list = list(range(1, 101))

# 1부터 100까지의 숫자에서 홀수들의 합을 구해서 출력 하시오
# 평균도 구해서 출력 하시오

odd_sum = 0
odd_count = 0

for num in num_list:
    if num % 2 == 1:
        odd_sum = odd_sum + num
        odd_count = odd_count + 1

odd_average = odd_sum / odd_count

print("홀수의 합 :", odd_sum)
print("홀수의 평균 :", odd_average)


