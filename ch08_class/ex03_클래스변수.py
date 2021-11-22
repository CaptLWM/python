class Car():
    # 클래스 변수
    instance_count = 0

    # 클래스 초기화 함수
    def __init__(self, size, color):
        self.size = size
        self.color = color
        Car.instance_count = Car.instance_count+1
        print("자동차 객체의 수 : {0}".format(Car.instance_count))

    # 클래스 함수
    def move(self):
        print("자동차({0} & {1})가 움직입니다".format(self.size, self.color))


# 객체 생성
car1 = Car('small', 'white')
car2 = Car('big', 'black')

print("Car 클래스의 총 인스턴스 개수:{}".format(Car.instance_count))

# 클래스 변수도 객체를 생성한 후, '객체명.변수명' 형식으로 접근할 수 있다.
print("Car 클래스의 총 인스턴스 개수:{}".format(car1.instance_count))

print("Car 클래스의 총 인스턴스 개수:{}".format(car2.instance_count))

car1.move()
car2.move()

# 클래스 변수 vs. 인스턴스 변수


class Car2():
    # 클래스 변수
    count = 0

    # 초기화 함수
    def __init__(self, size, num):
        # 인스턴스 변수
        self.size = size
        self.count = num
        Car2.count = Car2.count + 1  # 클래스 변수 이용
        print("자동차 객체의 수 : Car2.count = {0}".format(Car2.count))
        # 클래스 변수
        print("인스턴스 변수 초기화 : self.count = {0}".format(self.count))
        # 인스턴스 변수

    def move(self):
        print("자동차({0} & {1})가 움직입니다.".format(self.size, self.count))


car1 = Car2("sedan", 20)
'''
자동차 객체의 수 : Car2.count = 1 (클래스 안에)
인스턴스 변수 초기화 : self.count = 20 (객체 안에)
'''
car2 = Car2("SUV", 30)
'''
자동차 객체의 수 : Car2.count = 2
인스턴스 변수 초기화 : self.count = 30
'''
