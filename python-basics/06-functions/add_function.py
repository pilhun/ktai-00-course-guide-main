# def는 다시 사용할 기능에 이름을 붙입니다. 아래 두 값은 함수를 부를 때 전달받습니다.
def add_numbers(first, second):
    # return은 계산한 값을 함수를 부른 곳으로 돌려줍니다. 화면 출력과는 다릅니다.
    return first + second

# 함수를 정의하는 것만으로 실행되지는 않습니다. 괄호 안에 값을 넣어 호출합니다.
result = add_numbers(3, 5)
print("합계:", result)
# 같은 기능에 다른 숫자를 전달해 다시 사용할 수 있습니다.
print("다른 합계:", add_numbers(10, 20))
