# num_list = [1, 2, 3, 4, 5]
# # 코파일럿으로 변환
# num_list = list(range(1, 101))

# # print(num_list[0]) # 1번째
# # print(num_list[1]) # 2번째
# # print(num_list[2]) # 3번째
# # print(num_list[3]) # 4번째
# # print(num_list[4]) # 5번째

# # 1부터 100까지의 숫자에서 홀수만 출력 하세요

# # for num in num_list:
# #     print(num)

# for num in num_list:
#     if num % 2 == 1:
#         print(num)

# 홀수들의 합을 구해서 출력하시오      

# num_list = list(range(1, 101))

# total = 0
# for num in num_list:
#     if num % 2 == 1:
#         total = total + num

# print("홀수의 합 :", total)


# 짝수들의 합을 구해서 출력하시오

num_list = list(range(1, 101))

even_total = 0
for num in num_list:
    if num % 2 == 0:
        even_total = even_total + num

print("짝수의 합 :", even_total)

