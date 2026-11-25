# 직접 시도한 뒤 비교하는 풀이입니다. 바뀐 한 줄과 출력 결과를 확인합니다.
def double_number(number):  # 전달받은 수를 두 배로 만드는 함수입니다.
    return number * 2

result = double_number(5)  # 10을 돌려받아 result에 저장합니다.
print("함수 결과:", result)
print("하나 더한 값:", result + 1)  # return 값은 다른 계산에도 쓸 수 있습니다.
