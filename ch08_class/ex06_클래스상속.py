# 클래스 상속
# 형식 : class 자식클래스 이름(부모클래스 이름):
#              <코드블록>

# 부모 클래스
class Bicycle():
    # 초기화 함수(인스턴스 메소드)
    def __init__(self, wheel_size, color):
        # 인스턴스 변수
        self.wheel_size = wheel_size
        self.color = color

    def move(self, speed):
        print("자전거 : {0}km/h, 전진".format(speed))

    def turn(self, direction):
        print("자전거 : {0}".format(direction))

    def stop(self):
        print("자전거({0},{1}) : 정지".format(self))

# 자식 클래스


class FoldingBicycle(Bicycle):
    def __init__(self, wheel_size, color, state):
        #Bicycle.__init__(self, wheel_size, color)
        super().__init__(wheel_size, color)
        self.state = state

    def fold(self):
        self.state = 'folding'
        print("자전거: 접기, state={0}".format(self.state))

    def unfold(self):
        self.state = 'unfolding'
        print("자전거: 펴기, state={0}".format(self.state))


# 객체 생성
folding_bicycle = FoldingBicycle(27, 'black', 'folding')
folding_bicycle.move(40)
folding_bicycle.fold()
folding_bicycle.unfold()
