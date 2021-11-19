# 형식 지정 출력
# 나머지 연산자(%)를 이용한 형식 및 위치 지정
# 형식 : print("%type" %data)
#        print("%type %type", %(data1, data2))
# %s 문자열, %d 정수, %f 실수

name = "광재"
print("%s는 나의 친구 입니다." %name)

r =3
pi = 3.141592
print("반지름 : %d, 원주율 : %f" %(r, pi))

# 형식 지정 문자열에서 출력 위치 지정
# 형식 : print("{0} {1} {2}...{n}". format(data_0, data_1,...data_n))

animal_0 = "cat"
animal_1 = "dog"
animal_2 = "fox"

print("Animal : {0}".format(animal_0))
print("Animal : {0},{1},{2}".format(animal_0, animal_1, animal_2))
print("Animal : {0},{1},{2}".format(animal_0, animal_1, animal_0))
"""
Animal : cat
Animal : cat,dog,fox
Animal : cat,dog,cat
"""

print("Animal : {},{},{}".format(animal_0,animal_1,animal_2))

name="Thomas"
age = 10
a = 0.123456789
fmt_string = "String : {0}, Integer Number : {1}, Floating : {2}"
print(fmt_string.format(name, age, a))

# 형식 지정 문자열에서 숫자 출력 형식 지정
a=0.1234567890123456789
print("{0:.2f}, {0:.5f}".format(a)) # 0.12, 0.12346


