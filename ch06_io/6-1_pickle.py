# pickle 모듈을 이용하여 리스트와 클래스 저장하기
colors = ['red','green','black']
print(colors)
# ['red','green','black']
import pickle
f = open('./ch06_io/colors','wb')
pickle.dump(colors,f)
f.close()

class test:
    var = None

a = test() # test객체 생성
a.var = 'Test'

f = open('./ch06_io/test','wb')
pickle.dump(a,f)
f.close()

f = open('./ch06_io/test','rb')
b = pickle.load(f)
f.close()

print(b) # <__main__.test object at 0x037F1FD0>
print(b.var) # Test