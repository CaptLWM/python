# -*- coding:utf-8 -*-
# 오류는 어떨 때 발생하는가?
# 1. 디렉토리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류
# f = open("없는파일.txt" 'r')
'''
Traceback (most recent call last):
File "D:/dev/workspace/workspace-pycharm/foundation/ch08_exceptionHandler/ex01_error.py", line 6, in <module>
f = open("없는파일.txt" 'r')
FileNotFoundError: [Errno 2] No such file or directory: '없는파일.txtr'
'''
# 2. 0으로 다른 숫자를 나누는 경우에 발생하는 오류
# 4 / 0
'''
Traceback (most recent call last):
File " D:/dev/workspace/workspace-pycharm/foundation/ch08_exceptionHandler/ex01_error.py", line 14, in <module>
4 / 0
ZeroDivisionError: division by zero
'''
# 3. a[4]는 a 리스트에서 얻을 수 없는 값이여서 발생하는 오류
a = [1, 2, 3]
print(a[4])
'''
Traceback (most recent call last):
File " D:/dev/workspace/workspace-pycharm/foundation/ch08_exceptionHandler/ex01_error.py", line 24, in <module>
print(a[4])
IndexError: list index out of range
'''
