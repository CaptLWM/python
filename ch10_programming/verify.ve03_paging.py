# -*- coding: utf-8 -*-
# 게시판 페이징하기
def getTotalPage(m, n):
    if m % n == 0:
        return m//n
    else:
        return m//n + 1


    # 이 위치에 코드를 작성한다.
print(getTotalPage(5, 10))  # 1
print(getTotalPage(15, 10))  # 2
print(getTotalPage(30, 10))  # 3
