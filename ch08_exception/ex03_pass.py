# -*- coding:utf-8 -*-
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:  # 파일이 없더라도 오류를 발생시키지 않고 통과한다.
    pass
