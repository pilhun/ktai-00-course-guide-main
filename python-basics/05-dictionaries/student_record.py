# 딕셔너리는 키(이름표)와 값의 쌍을 중괄호 안에 저장합니다.
student = {"name": "민지", "age": 20}
# name과 age는 이 자료 안에서 값을 찾는 키입니다. 키에는 따옴표를 붙입니다.
print("이름:", student["name"])
print("나이:", student["age"])
# 기존 키에 새 값을 넣으면 그 값이 바뀝니다.
student["age"] = 21
print("바꾼 나이:", student["age"])
