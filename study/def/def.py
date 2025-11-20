"""
def add(a,b):
    return a + b

print(f"result : {add(3,5)}")

def add_many(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"result2 : {add_many(1,2,3,4,5)}")
print(f"result3 : {add_many(1,2,3,4,5,6,7,8,9,10)}")

def print_kwargs(**kwargs): # 딕셔너리 형태로 출력
    for k, v in kwargs.items():
        print(f"{k} : {v}" )

print_kwargs(name="Alice", age=30, city="New York")

def add_and_multiply(a, b):
    return (a + b) , a*b

result4, result5 = add_and_multiply(3, 5)
print(f"result4 : {result4}, result5 : {result5}")

def say_myself(name, age, man=True): # name, man=True, age => 안됨, 초기화 하고 싶은 매개변수는 항상 뒤에
    print("나의 이름은 %s 입니다." % name) 
    print("나이는 %d살입니다." % age) 
    if man: 
        print("남자입니다.") 
    else: 
        print("여자입니다.")
"""

def dofunc1():
    print('dofunc1호출')

def dofunc2(name):
    print('안녕', name)

def dofunc3(arg1, arg2):
    res = arg1 + arg2
    return res
print('.............')
dofunc1()
print('...')
dofunc1()
print(dofunc1) # 함수 주소
other = dofunc1
other()

print(dofunc2('한국인'))

print(dofunc3(10, 20))
print(dofunc3('파이썬','만세'))

print('현재 파일의 객체 목록 : ', globals())