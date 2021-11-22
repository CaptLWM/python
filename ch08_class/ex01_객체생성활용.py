# 클래스 선언
class Bicycle():

    # Bicycle 클래스에 함수를 추가한다.
    # 클래스 함수(메소드)
    def mov(self, speed):
        print("자전거: 시속 {0}킬로미터로 전진".format(speed))

    def turn(self, direction):
        print("자전거:{0}회전".format(direction))

    def stop(self):
        print("자전거({0}, {1}) : 정지".format(self.wheel_size, self.color))

    # pass = continue와 비슷


# 객체생성
# 객체명 = 클래스명()
my_bicycle = Bicycle()
print(my_bicycle)  # <__main__.Bicycle object at 0x03981FB8>

# 객체에 속성 설정
# 객체명.변수명 = 속성값
# 별도로 변수 선언 안해도 사용할 수 있음
my_bicycle.wheel_size = 26
my_bicycle.color = 'black'

print("바퀴크기 :", my_bicycle.wheel_size)  # 바퀴크기 : 26
print("색상 :", my_bicycle.color)  # 색상 : black

my_bicycle.mov("40")
my_bicycle.turn("우")
my_bicycle.stop()

# 객체생성
bicycle1 = Bicycle()
bicycle1.wheel_size = 24
bicycle1.color = "brown"

bicycle1.mov(20)
bicycle1.turn("좌")
bicycle1.stop()

bicycle2 = Bicycle()
bicycle2.wheel_size = 18
bicycle2.color = "red"

bicycle2.mov(90)
bicycle2.turn("우")
bicycle2.stop()
