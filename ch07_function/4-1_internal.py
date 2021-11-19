# 유용한 내장함수
# 형 변환 함수

# 정수형으로 변환
print([int(0.123), int(3.51233), int(-1.3123464)])
# [0,3,-1]

# 실수형으로 변환
print([float(0), float(123), float(-64)])
#[0.0, 123.0, -64.0]

#문자형으로 변환
print([str(123), str(45678), str(-123)])
# ['123', '45678', '-123']]

# 리스트, 튜플, 세트형으로 변환
list_data = ['abc', 1,2, 'def']
tuple_data = ('abc', 1,2, 'def')
set_data = {'abc', 1,2, 'def'}

print([type(list_data), type(tuple_data), type(set_data)])
# [<class 'list'>, <class 'tuple'>, <class 'set'>]

print("리스트로 변환 : ", list(tuple_data), list(set_data))
# 리스트로 변환 :  ['abc', 1, 2, 'def'] ['abc', 1, 2, 'def']

print("튜플로 변환 : ", tuple(list_data), tuple(set_data))
# 튜플로 변환 :  ('abc', 1, 2, 'def') ('def', 1, 2, 'abc')

print("셋으로 변환 : ", set(list_data), set(tuple_data))
# {'def', 1, 2, 'abc'} {'abc', 1, 2, 'def'}

# bool 함수
# 숫자를 인자로 bool 함수 호출
print(bool(0)) # F
print(bool(1)) # T
print(bool(-1)) # T

# 문자열을 인자로 bool 함수 호출
print(bool('a')) # T
print(bool(' ')) # T 빈칸도 값이 있기때문
print(bool('')) # F
print(bool(None))

# 리스트, 튜플, 세트를 인자로 bool 함수 호출
myFriends=['james','robert']
print(bool(myFriends)) # T

myNum = ()
print(bool(myNum)) # F

mySetA={}
print(bool(mySetA)) # F

#bool 함수의 활용
def print_name(name):
    if bool(name):
        print("입력된 이름: ", name)
    else:
        print("입력된 이름이 없습니다.")

print_name("james")
print_name("")

# 최솟값과 최대값을 구하는 함수
myNum = [10,5,12,0,3.5,99.5,42]
print([min(myNum), max(myNum)])

myStr = "adffad"
print([min(myStr), max(myStr)])

myNum = ["ABC", "abc", "bcd","efg"]
print([min(myNum), max(myNum)])

# 절대값과 전체 합을 구하는 하무
print([abs(10), abs(-10)])
SumList = [1,2,3,4,5,6,7,8,9]
print(sum(SumList))

# 항목의 갯수를 구하는 함수
print(len("ab" "cd"))
print(len([1,2,3,4,5,6,7,8]))
print(len({1:"Thomas", 2:"Edward"}))

# 내장함수의 활용
scores = [90,80,95,85]

score_sum = 0
subject_num = 0
for score in scores:
    score_sum = score_sum + score
    subject_num = subject_num + 1
average = score_sum / subject_num
print("총점:{0}, 평균 {1}".format(score_sum, average))

scores = [90,80,95,85]
print("총점:{0}, 평균 {1}".format(sum(scores), sum(scores)/len(scores)))

print("최하점수:{0}, 최고점수:{1}".format(sum(scores), sum(scores)/len(scores)))


print("\n*** 재귀적 함수 호출 ***")
def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)
    # 3! = 3x2!
print(factorial(4))

# Tower of Hanoi
def hanoi(ndisks, startPeg=1, endPeg=3):
    if ndisks:
        hanoi(ndisks-1, startPeg, 6-startPeg-endPeg)
        print(startPeg, "번 기둥의", ndisks, "번 원반을", endPeg, "번 기둥에 옮깁니다.")
        hanoi(ndisks-1, 6-startPeg-endPeg, endPeg)
hanoi(ndisks=5)
