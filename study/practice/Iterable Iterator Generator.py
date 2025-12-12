'''
    Iterable 객체
        - 반복 가능한 객체
        - list, dict, set, str, bytes, tuple, range

    Iterator
        - Iterator 객체 : 값을 차례대로 꺼낼 수 있는 객체
        - iterable한 객체를 내장함수 또는 iterable객체의 메소드로 객체 생성 가능
        - 파이썬 내장함수 iter() 사용
'''

a = [1,2,3]
a_iter = iter(a)
print(type(a_iter)) # <class 'list_iterator'>

b={1,2,3}
print(dir(b)) # iterable 객체는 매직메소드 __iter__ 가지고 있음
b_iter = b.__iter__()
print(type(b_iter)) # <class 'set_iterator'>

# next() 하나씩 값 뽑아냄
print(next(a_iter)) # 1
print(next(a_iter)) # 2
print(next(a_iter)) # 3
#print(next(a_iter)) # StopIteration, 예외 발생, 더 나올게 없기 때문

'''
    
'''
