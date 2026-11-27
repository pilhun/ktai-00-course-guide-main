# 개인별로 지금까지 공부하신 내용을 기반으로 문제를 만든다
# 해당문제를 본인이 풀어보고 discord 의 커뮤니티에는 문제만 올린다

# [문제] 가상분식 영수증 
# 가상분식 사장님이 오늘 주문 금액 4건을 영수증처럼 정리하고 싶어 합니다.

# num_list = [3500, 4000, 2500, 5000]


# 아래처럼 출력하세요. (실행후 나올 답)

# 1번 주문 : 3500원
# 2번 주문 : 4000원
# 3번 주문 : 2500원
# 4번 주문 : 5000원
# 합계 : 15000원
# 평균 : 3750.0원


# 조건
# f-string 사용 (중요하다고 해서 넣음)
# 주문 번호는 1번부터 시작
# 마지막에 합계와 평균 출력

num_list = [3500, 4000, 2500, 5000]

num_count = 0
num_sum = 0

for num in num_list:
    num_count = num_count + 1
    num_sum = num_sum + num
    print(f"{num_count}번 주문 : {num}원")

average = num_sum / len(num_list)
print(f"합계 : {num_sum}원")
print(f"평균 : {average}원")


