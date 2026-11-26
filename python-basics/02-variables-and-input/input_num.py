print("start1")
num1 = 100
print("start2")
num2 = input("enter an integer a decimal number: ")
print("start3")
# float > int
try:
    num2 = float(num2)
    result = num1 + float(num2)
    print("start4")
    print("the result is:", result)
except ValueError:
    print("숫자를 입력하세요")

print("end")

