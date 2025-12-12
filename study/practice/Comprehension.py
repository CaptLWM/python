'''
    컴프리헨션(Comprehension)
    - 파이썬의 자료구조(list, dictionary, set)에 데이터를 좀 더 쉽고 간결하게 담기 위한 문법
'''

# list comprehension
squares = [n*n for n in range(1, 6)]
print(squares) #[1, 4, 9, 16, 25]

squares2 = [i for i in range(1, 11) if i % 2 == 0 if i < 5] # if문도 가능
print(squares2) #[2, 4]

squares3 = [(x, y) for x in range(1, 6) for y in range(1, 4)] # for문 중첩도 가능
print(squares3) #[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3), (4, 1), (4, 2), (4, 3), (5, 1), (5, 2), (5, 3)]

'''
    list 함수
    squares2 = list(range(1,11))
    print(squares2) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

# dict comprehension
data = {"a": 1, "b": 2, "c": 3}
rev = {v: k for k, v in data.items()} # key : value 뒤집기
print(rev) #{1: 'a', 2: 'b', 3: 'c'}

data2 = {i : i*2 for i in range(1, 6)}
print(data2) #{1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

name = ["왕춘삼", "김덕팔", "황갑득"]
age = [23, 14, 42]
data3 = {key: value for (key, value) in zip(name, age) if value > 20}
print(data3) #{'왕춘삼': 23, '황갑득': 42}

#set comprehension
setData = {i for i in range(1, 11)}
print(setData) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
