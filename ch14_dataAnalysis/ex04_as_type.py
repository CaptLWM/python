# 배열의 데이터 타입 변환
import numpy as np

print(np.array(['1.5','0.62','2','3.14','3.141231']))
# ['1.5' '0.62' '2' '3.14' '3.141231']

str_a1 = np.array(['1.123','0.123','5.123','9', '8'])
num_a1 = str_a1.astype(float)
print(num_a1)
# [1.123 0.123 5.123 9.    8.   ]

print(str_a1.dtype) # <u5 / 유니코드 문자
print(num_a1.dtype) # float64 / 실수

str_a2 = np.array(['1','3','5','7','9'])
num_a2 = str_a2.astype(int)

print(num_a2)
#[1 3 5 7 9]

print(str_a2.dtype) # <u1
print(num_a2.dtype) # int64

num_f1 = np.array([10,21,0.53,123, 1.23])
num_i1 = num_f1.astype(int)
print(num_i1)

print(num_f1.dtype)
print(num_i1.dtype)