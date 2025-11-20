# 딕셔너리 자료형
def func(w,h,**other):
    print('몸무게 {}, 키 {}'.format(w,h))
    print(other)

func(65, 180, irum='지구인', nai=23)

# 혼합도 가능
def functional(a,b,*v1, **v2):
    print(a,b)
    print(v1)
    print(v2)

functional(1,2)
functional(1,2,3,4,5)
functional(1,2,3,4,5, m=6, n=7)