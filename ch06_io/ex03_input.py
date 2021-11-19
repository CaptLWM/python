# 키보드 입력
# 형식 : data = input("문자열")

yourName = input("당신의 이름은?")
print("당신은 {} 입니다".format(yourName))

num = input("숫자를 입력하세요")
print("당신이 입력한 숫자는 {} 입니다.".format(num))

a = input("정사각형 한 변의 길이는? ")
area = int(a) ** 2 # string->int
print("정사각형 넓이 : {}".format(area))

b = input("정사각형 한 변의 길이는?")
area = float(b)**2
print("정사각형 넓이 : {}".format(area))