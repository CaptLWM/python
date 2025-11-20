def func1(*ar): # * 가변 인수 처리, 여러개 받을 수 있음
    print(ar)
    for i in ar:
        print('음식 : ', + i)

func1(1,2,3,4,5)

def func2(a, *ar): # *ar, a는 에러 발생 => a에는 매핑 안되기 때문
    print(a, ar)

func2(1,2,3,4,5)