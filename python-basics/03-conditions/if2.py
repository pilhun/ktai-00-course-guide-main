# 두개의 수를 입력 받아서 
# 합이 10보다 크면 "합이 10보다 큽니다."를 출력하고
# 합이 10보다 작거나 같으면 "합이 10보다 작거나 같습니다

num1 = input("첫 번째 수: ")
num2 = input("두 번째 수: ")

total = float(num1) + float(num2)

if total > 10:
    print("합이 10보다 큽니다.")
else:
    print("합이 10보다 작거나 같습니다.")
