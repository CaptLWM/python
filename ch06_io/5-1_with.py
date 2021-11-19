# with 문을 이용해 파일 읽고 쓰기
# with 문의 구조
f = open("./ch06_io/myFile.txt",'w')
f.write('File write/read test.')
f.close()

# with문 활용
with open('./ch06_io/myFile4.txt','w',encoding='utf-8') as f: # 인코딩 방식 설정
    f.write('한글 test1: line1\n')
    f.write('한글 test2: line2\n')
    f.write('한글 test3: line3\n')
'''
�ѱ� test1: line1
�ѱ� test2: line2
�ѱ� test3: line3
인코딩 949 방식이라 한글 깨짐
'''

with open('./ch06_io/myFile2.txt','r') as f:
    file_string = f.read()
    print(file_string)
    '''
    File read/write test2: line1
    File read/write test2: line2
    File read/write test2: line3
    '''

with open('./ch06_io/myFile3.txt','w') as f:
    for num in range(1,6):
        format_string = "3 x {0}={1}\n".format(num, num*3)
        f.write(format_string)

with open('./ch06_io/myFile3.txt','r') as f:
    for line in f: # f.readlines()와 같다.
        print(line, end="")

