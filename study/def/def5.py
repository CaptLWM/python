"""
# nonlocal
def kbs():
    a=1 # 지역함수
    def mbc():
        nonlocal a # 외부함수인 kbs의 a
        print(a) # 1 출력
        a=2
    mbc()
kbs()

# global
b = 1
def sbs():
    global b # b 전역변수
    print(b)
    b=2
sbs()
"""

a=10; b=20; c=30
print('함수 수행 전 a:{}, b:{}, c:{}'.format(a,b,c))

def foo():
    a=40; b=50

    def bar():
        # b = 60
        # c = 70
        nonlocal b
        global c
        print('bar에서 출력1 a:{}, b:{}, c:{}'.format(a,b,c))
        b=80
        print('bar에서 출력2 a:{}, b:{}, c:{}'.format(a,b,c))
        c=90
        print('bar에서 출력3 a:{}, b:{}, c:{}'.format(a,b,c))

    bar()

    print('foo에서 출력 a:{}, b:{}, c:{}'.format(a,b,c))

foo()
print('함수 수행 후 a:{}, b:{}, c:{}'.format(a,b,c))