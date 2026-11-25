# 오류를 확인한 뒤 비교하는 선택 풀이입니다.
student = {"name": "민지", "age": 20}
score = 80
print("0. 정상 / 1. 숫자 변환 / 2. 변수 이름 / 3. 딕셔너리 키")
case = input("실행할 사례> ")
if case == "0":
    print(student["name"])
elif case == "1":
    # try 안에서 숫자 변환이 실패하면 except에서 안내합니다. 선택 심화 문법입니다.
    try:
        number = int(input("숫자(정수)> "))
    except ValueError:
        print("숫자로 입력해 주세요.")
    else:
        print(number)
elif case == "2":
    print(score)  # 처음 만든 변수와 같은 철자를 사용합니다.
elif case == "3":
    print(student["name"])  # 실제로 들어 있는 키를 사용합니다.
else:
    print("0부터 3까지 선택합니다.")
