class Car():
    # 클래스 변수
    instance_count = 0

    # 초기화 함수(인스턴스 메소드)
    def __init__(self, size, color):
        # 인스턴스 변수
        self.size = size
        self.color = color
        Car.instance_count = Car.instance_count + 1
        print("자동차 객체의 수: {0}".format(Car.instance_count))

    # 인스턴스 메소드:
    # - 각 객체에서 개별적으로 동작하는 함수
    # - 첫 인자로 self가 필요함
    def move(self, speed):
        self.speed = speed
        print("자동차({0} & {1})가".format(self.size, self.color), end='')
        print("시속 {0}킬로미터로 달립니다.".format(self.speed))

    # 정적 메소드
    # - 클래스나 클래스의 인스턴스와는 무관하게 독립적으로 동작하는 함수
    # - self를 사용하지 않으며 정적 메소드 안에서는 인스턴스 메소드나 인스턴스 변수를
    #   접근할 수 없다.
    @staticmethod  # 선언 필수
    def check_type(model_code):
        if(model_code >= 20):
            print("이 자동차는 전기차입니다.")
        elif(10 <= model_code < 20):
            print("이 자동차는 가솔린입니다.")
        else:
            print("이 자동차는 디젤입니다.")

    # 클래스 메소드
    # - 클래스 변수를 사용하기 위한 함수
    # - 첫번째 인자로 클래스를 넘겨받는 cls가 필요
    # - @classmethod를 지정
    @classmethod
    def count_instance(cls):
        print("자동차 객체의 개수 : {0}".format(cls.instance_count))


car1 = Car("small", "red")
car2 = Car("big", 'green')

car1.move(90)
car2.move(100)


car1.check_type(2)
car2.check_type(23)


Car.count_instance()  # 객체 생성 전에 클래스 메소드 호출

car1 = Car("small", "red")
Car.count_instance()
car2 = Car("small", "red")
Car.count_instance()
car3 = Car("small", "red")
Car.count_instance()
