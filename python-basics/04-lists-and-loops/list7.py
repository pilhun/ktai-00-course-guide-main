# # [문제] 가상카페 하루 매출 정리

# 아래는 가상카페의 오늘 주문 금액 10건입니다.

# prices = [4500, 5000, 3800, 6000, 5500, 4200, 7000, 3000, 4800, 5200]

# 1. 주문 건수와 총 매출을 출력하세요.
# 2. 5,000원 이상인 주문만 골라 출력하고, 그 건수와 평균 금액(소수 첫째 자리까지)을 구하세요. (5,000원 이상이 하나도 없으면 "없습니다"를 출력)
# 3. 가장 비싼 주문과 가장 싼 주문을 출력하세요.
# 4. 비싼 순서대로 상위 3개를 출력하세요. (원본 리스트는 바뀌면 안 됩니다)
# 5. 총 매출이 50,000원 이상이면 "목표 달성", 40,000원 이상이면 "거의 도달", 그 미만이면 "내일 더 힘내요"를 출력하세요.

# 조건: 출력은 f-string을 사용하세요.

# [도전, 선택] 기준 금액을 input으로 받아, 그 금액 이상인 주문만 출력하세요.
# (숫자가 아니거나 0 이하이면 안내 문구를 출력하고 종료)

prices = [4500, 5000, 3800, 6000, 5500, 4200, 7000, 3000, 4800, 5200]

total = sum(prices)
print(f"주문 건수 : {len(prices)}건")
print(f"총 매출 : {total}원")

base = 5000
big_sum = 0
big_count = 0
for price in prices:
    if price >= base:
        print(f"{base}원 이상 주문 : {price}원")
        big_sum += price
        big_count += 1

if big_count == 0:
    print(f"{base}원 이상 주문이 없습니다.")
else:
    big_average = big_sum / big_count
    print(f"{base}원 이상 주문 {big_count}건, 평균 {big_average:.1f}원")

print(f"가장 비싼 주문 : {max(prices)}원 / 가장 싼 주문 : {min(prices)}원")
print(f"비싼 순 상위 3개 : {sorted(prices, reverse=True)[:3]}")

if total >= 50000:
    print("오늘 목표 달성!")
elif total >= 40000:
    print("목표에 거의 도달했습니다.")
else:
    print("내일 더 힘내요.")
