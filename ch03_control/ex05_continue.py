for k in range(5):
    if(k==2):
        continue #2빼고 나머지 출력
    print(k)

k=0
while True:
    k=k+1
    if(k==2):
        print("continue next")
        continue
    if(k>4):
        break
    print(k)
    