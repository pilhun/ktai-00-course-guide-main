# 4개의 숫자를 입력 받아서
# 평균과 합계를 계산하는 프로그램을 작성하세요.
# 출력은 결과는 평균 10.3 합계는 41.2 입니다. 와 같이 출력합니다.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num3 = input("Enter the third number: ")
num4 = input("Enter the fourth number: ")
total = float(num1) + float(num2) + float(num3) + float(num4)
average = total / 4
# () {} []
print(f"결과는 평균 {average} 합계는 {total} 입니다.")