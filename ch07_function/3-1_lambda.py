# 람다(lambda) 함수 : 익명의 함수식
# 형식 : lambda <인자> : <인자 활용 수행 코드>
#        lambda <인자> : <인자 활용 수행 코드> (<인자>)
def exp(x):
    return x**2

# 1. exp(3) 함수 호출
print(exp(3))

# 2. 익명의 함수를 람다식으로 표현
print((lambda x : x**2)(3))

# 3. 익명 함수를 변수에 지정하여 이름을 부여
mySquare = lambda x: x**2
print(mySquare(3))