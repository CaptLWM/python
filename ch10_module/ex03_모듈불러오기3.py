from my_area import circle_area as circle
from my_area import square_area as square
from my_area import PI as pi
import my_area as area

from my_module1 import *
from my_module2 import *

func1()
func2()  # module1,2 에 겹침 => module2에 func2가 실행 => 나중에 import된 항목이 실행
func3()
'''
func1 in my_module1
func2 in my_module2
func3 in my_module2
'''

# 모듈명을 별명으로 선언
# from 모듈명 import 변수명 as 별명
# from 모듈명 import 함수명 as 별명
# from 모듈명 import 클래스명 as 별명

print('pi=', area.PI)
print('square area=', area.square_area(2))
print('circle area=', area.circle_area(2))


print('pi=', pi)
print('square area=', square(2))
print('circle area=', circle(2))
