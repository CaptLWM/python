# 함수의 기본 구조
# 형식 : def 함수명([인자1, 인자2,...,인자n]):
#       <코드블록>
#       return <반환 값>

# 인자도 반환값도 없는 함수
# 함수 정의
def my_func():
    print("My first function!")
    print("This is a function")

my_func() # 함수 호출

# 인자는 있으나 반환 값이 없는 함수
def my_friend(friendName):
    print("{}는 나의 친구입니다.".format(friendName))

my_friend("철수")
my_friend("영미")
my_friend("갑수")

def my_student_info(name, school_ID, phoneNumber):
    print('-------------------')
    print('- 학생이름: ', name)
    print('- 학급번호: ', school_ID)
    print('- 전화번호: ', phoneNumber)

my_student_info("현아","01","10-123-1234")
my_student_info("진수","03","56-123-1234")

# 인자도 있고 반환 값도 있는 함수
def my_calc(x,y):
    z = x * y
    return z

print(my_calc(3,4)) # 12

def my_student_info_list(student_info):
    print("***************************")
    print("- 학생이름:", student_info[0])
    print("- 학급번호:", student_info[1])
    print("- 전화번호:", student_info[2])
    print("***************************")

student1_inf = ["현아","01","01-12-123"]
my_student_info_list(student1_inf)
my_student_info_list(["진수","03","56-123-1234"])