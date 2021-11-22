# 모듈을 불러오는 다른 형식
# import 모듈
# from 모듈 import 변수명
# from 모듈 import 함수명
# from 모듈 import 클래스명

from my_area import PI
# from my_area import square_area
# from my_area import circle_area
from my_area import *  # *쓰면 모듈 안에 모든걸 불러오겠다는 뜻

print('pi=', PI)  # pi= 3.14

print('square area =', square_area(5))  # 모듈의 함수 이용 square area = 25
print('circle area =', circle_area(5))  # 모듈의 함수 이용 circle area = 78.5
