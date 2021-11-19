# 1
input1 = input("첫번째 숫자를 입력하세요: ")
input2 = input("두번째 숫자를 입력하세요: ")
total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다." %total)
# 출력결과 36

# 2
f1 = open("./ch06_io/test.txt", 'w')
f1.write("Life is too short\nyou need java")
f1.close()
f2 = open("./ch06_io/test.txt", 'r')
print(f2.read())
f2.close()


# 3
user_input = input("저장할 내용을 입력하세요: ")
f = open("./ch06_io/test.txt", 'a')
f.write("\n") ## 입력한 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입 3 / 5
f.write(user_input)
f.close()

# 4
'''
Life is too short
you need java
'''
f = open('./ch06_io/test.txt', 'r')
body = f.read() # test.txt 파일의 내용을 body 변수에 저장
f.close()
body = body.replace('java','python') # body 문자열에서 'java'를 'python'으로 변경
f = open('./ch06_io/test.txt', 'w') # 파일을 쓰기 모드로 다시 실행
f.write(body)
f.close()

# 5
f = open("./ch06_io/sample.txt")
lines = f.readlines() # sample.txt를 줄 단위로 모두 읽는다.
f.close()
total = 0
for line in lines:
    score = int(line)
    total += score
average = total/len(lines)
f = open("./ch06_io/result.txt", 'w')
f.write(str(average))
f.close()