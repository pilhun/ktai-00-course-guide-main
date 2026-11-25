# 선택 오류 연습입니다. 먼저 0으로 정상 실행을 확인합니다.
student = {"name": "민지", "age": 20}
score = 80
print("0. 정상 / 1. 숫자 변환 / 2. 변수 이름 / 3. 딕셔너리 키")
case = input("실행할 사례> ")
if case == "0":
    print(student["name"])
elif case == "1":
    # 정수 대신 글자를 입력하면 일부러 ValueError를 확인할 수 있습니다.
    number = int(input("숫자(정수)> "))
    print(number)
elif case == "2":
    # score와 scores의 철자가 다릅니다. 일부러 NameError가 나게 했습니다.
    print(scores)
elif case == "3":
    # text 키가 없어 일부러 KeyError가 발생합니다. 실제 키 목록과 대조합니다.
    print(student["text"])
else:
    print("0부터 3까지 선택합니다.")
