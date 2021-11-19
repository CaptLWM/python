# 변수의 범위 : 함수 안에서 정의한 변수는 함수 안에서만 사용 가능

a=5 #전역변수

def func1():
    a = 1 #지역변수
    print("[func1] 지역변수 a =", a)

func1() # a = 1
print(a) # a = 5

def func4():
    global a #전역변수를 함수 안으로
    a = 4 # 전역변수 변경 5->4
    print("[func4] 전역변수 a = ",a)

func4()
print(a)