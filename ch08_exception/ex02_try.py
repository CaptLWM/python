# -*- coding:utf-8 -*-
# 오류 예외 처리 기법
# try, except 문
try:
    4 / 0
except ZeroDivisionError as e:  # 예외처리(Exception Handler)
    # print(e)
    pass

# try ... finally
f = open("foo.txt", 'w')
try:
    pass
finally:  # 항상 실행해야하는 실행문을 기입한다.
    f.close()

# 여러 개의 오류 처리하기
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱할 수 없습니다.")
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
