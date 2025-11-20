player = '전국대표' # 전역변수

def funcsoccer():
    name = '홍길동' # 지역변수
    player = '지역대표' # 지역변수, 이런식으로 쓰지는 말것 가독성 떨어짐
    print(name, player)

funcsoccer()
print(player)

