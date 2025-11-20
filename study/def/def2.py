def area_tri(a,b):
    c = a * b / 2
    print('순서2')
    area_print(c)
    print('순서4')

def area_print(c):
    print('순서3')
    print('삼각형 면적', c)

print('순서1')
area_tri(20,30)
print('순서5')

def isodd(arg):
    return arg % 2 == 1


