from abc import ABC, abstractmethod # 추상클래스 쓰기 위해서는 반드시 필

'''
    클래스
'''
class Person:
    data = 4

p = Person()
print(p) #<__main__.Person object at 0x0000027F31CA5940>
print(p.data) #4

'''
    생성자
'''
class Person2:
    def __init__(self): # __init__ => 객체 생성될 때 자동으로 호출
        print("태어남..")

p = Person2() # 태어남..

class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1 # 객체 생성 될때마다 count 증가

    def get_count(self):
        return MyClass.count
    
a = MyClass()
b = MyClass()
c = MyClass()

print(a.get_count())

'''
    * 메서드 : 클래스 안에 정의된 함

    클래스 메서드/정적 메서드
    
    | 종류            | 첫 인자 | 용도                  |
    | --------------- | ------- | --------------------- |
    | 인스턴스 메서드 | self    | 인스턴스 상태 접근    |
    | 클래스 메서드   | cls     | 클래스 전체 상태 관리 |
    | 정적 메서드     | 없음    | 독립 기능 (유틸 함수) |

'''
# 인스턴스 메서드
class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1          # 인스턴스 상태 변경

c = Counter()
print('인스턴스메서드',c.count)
c.inc()
print('인스턴스메서드', c.count)  # 1

# 클래스 메서드

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        # "이름-나이" 같은 문자열을 받아 인스턴스 생성
        name, age = s.split("-")
        return cls(name, int(age))

p = Person.from_string("Wonmin-28")
print('클래스메서드',type(p), p.name, p.age)

# 정적 메서드

class MathUtil:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

print('정적',MathUtil.is_even(4))   # True

# 추상 메서드

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r * self.r

c = Circle(2)
print('추상',c.area())

# 메서드 동작 비교


class Base(ABC):
    @abstractmethod
    def must_impl(self):
        pass

    @classmethod
    def cls_method(cls):
        print("class method:", cls.__name__)

    @staticmethod
    def static_method():
        print("static method")

    def inst_method(self):
        print("instance method:", self)

class Impl(Base):
    def must_impl(self):
        print("implemented")

i = Impl()
i.must_impl()          # 인스턴스 메서드 호출
i.inst_method()        # 인스턴스 메서드
Impl.cls_method()      # 클래스 메서드, 클래스 이름 출력
Impl.static_method()   # 정적 메서드

'''
    클래스 상속
    - 중복코드 제거 + 기능 확장에도 사
'''

class Animal:
    def sound(self):
        return "unknown"

class Dog(Animal):
        def sound(self):
            return "woof"

print(Dog().sound()) # woof
