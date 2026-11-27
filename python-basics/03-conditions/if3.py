# 4개의 숫자를 입력 받는다
# 4개의 숫자 평균을 구한다
# 평균이 90점 이상이면 "A학점",
# 80점 이상이면 "B학점", 70점 이상이면 "C학점",
# 60점 이상이면 "D학점",그 외에는 "F학점"을 출력한다.

num1 = input("첫 번째 점수: ")
num2 = input("두 번째 점수: ")
num3 = input("세 번째 점수: ")
num4 = input("네 번째 점수: ")

total = float(num1) + float(num2) + float(num3) + float(num4)
average = total / 4

if average >= 90:
    print("A학점")
elif average >= 80:
    print("B학점")
elif average >= 70:
    print("C학점")
elif average >= 60:
    print("D학점")
else:
    print("F학점")

    