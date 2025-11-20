# 클로저
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner # 클로저, 내부함수의 주소 반환

# 함수 내의 count 확인
var1 = outer() # 객체 생성 후 내부 함수의 객체 주소 var1에 치환
print(var1()) # 변숫값 계속 유지
print(var1()) # 변수 count의 값 유지

var2 = outer() # 새로운 객체 생성
print(var2()) # count 초기화
print(id(var1))
print(id(var2)) # 주소값 확인 var1, var2 다름