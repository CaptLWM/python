# 파일 쓰기
# 형식:f=open('file_name', 'w')
#      f.write(str)
#      f.close()

f = open('./ch06_io/myFile.txt', 'w')
f.write('Thisisjusthis, this is my first file')
f.close

# 파일 읽기
# 형식 : f=open('file_name', 'r') 혹은 f=open('file_name')
#       data = f.read()
#       f.close()
f = open('./ch06_io/myFile.txt','r')
file_text=f.read()
f.close()
print(file_text)