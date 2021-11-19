# 반복문을 이용해 파일 읽고 쓰기

f = open('./ch06_io/two_times_table.txt', 'w')
for num in range(1,6):
    format_string = "2 x {0} = {1}\n".format(num, num*2)
    f.write(format_string)
f.close()
