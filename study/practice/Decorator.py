import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"실행 시간: {end - start:.5f}초")
        return result
    return wrapper
'''
@measure_time
def slow_function():
    time.sleep(0.5)
    return "done"
'''

def hello():
    print("hello")
    
def deco(fn):
    def deco_hello():
        print("*" * 20)    # 기능 추가
        fn()               # 기존 함수 호출
        print("*" * 20)    # 기능 추가
    return deco_hello

deco_hello = deco(hello)
deco_hello()

@measure_time
@deco
def hello2():
    print("hello2")

hello2()
