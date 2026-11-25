# 한 학생의 이름과 점수 두 개를 이름표로 구분합니다.
student = {"name": "민지", "korean": 80, "english": 90}
# 딕셔너리에서 숫자를 꺼낸 뒤 이미 배운 덧셈과 나눗셈을 사용합니다.
total = student["korean"] + student["english"]
average = total / 2
print("이름:", student["name"])
print("합계:", total)
print("평균:", average)
