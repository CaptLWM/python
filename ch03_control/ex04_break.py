# 반복문을 빠져나오는 break
k = 0
while True:
    k=k+1
    if(k>3):
        break   # while문을 빠져나옴
    print(k)


for k in range(10):
    if(k>2):
        break # for문을 빠져나옴
    print(k)