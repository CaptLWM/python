# -*- coding: utf-8 -*-
result = 0
# 이 위치에 코드를 작성한다.

for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n


print(result)
# 233168
