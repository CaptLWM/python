#단일 조건에 따른 분기(if)
x=95
if x>=90:
    print("축하합니다.")
    print("당신은 합격입니다.")
# 괄호 대신 들여쓰기로 구분/신경써서 해야함

# 단일조건 및 그 외 조건에 따른 분기(if~else)

x=75
if x>=90:
    print("pass")
else:
    print("Fail")

# 여러 조건에 따른 분기(if~elif~else)
x=85
if x>=90:
    print("Very Good")
elif (x>=80) and (x<90):
    print("Good")
else:
    print("Bad")

# 중첩조건에 따른 분기
x=100
if x>=90:
    if x==100:
        print("perfect")
    else:
        print("VeryGood")
elif(x>=80) and (x<90):
    print("good")
else:
    print("Bad")