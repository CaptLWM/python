# 난수발생모듈
# import random
# import random 모듈함수()
import random

print(random.random())  # 0~1사이의 임의의 실수

dice1 = random.randint(1, 6)  # 1~6 사이의 임의의 정수값
dice2 = random.randint(1, 6)

print('주사위 두개의 숫자:{0}, {1}'.format(dice1, dice2))

print(random.randrange(0, 11, 2))  # 0~11 사이 임의의 짝수

num1 = random.randrange(1, 10, 2)  # 1~9 사이 임의의 홀수
num2 = random.randrange(0, 100, 10)  # 0~90 사이 10의 배수
print('num1 {0} / num2 {1}'.format(num1, num2))

menu = ['비빔밥', '된장찌개', '볶음밥', '스파게티', '피자', '탕수육', '파스타']
print(random.choice(menu))  # 리스트에서 인자 선택

print(random.sample([1, 2, 3, 4, 5], 2))  # 모집단에서 두개의 인자 선택
