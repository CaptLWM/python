# 배열의 연산
# 기본 연산

import numpy as np

arr1 = np.array([10,20,30,40])
arr2 = np.array([1,2,3,4])

print(arr1 + arr2)
print(arr1 - arr2)

print(arr2 *2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1/(arr2 **2))
print(arr1>10)
'''
[2 4 6 8]
[ 10  40  90 160]
[10. 10. 10. 10.]
[10.          5.          3.33333333  2.5       ]
[False  True  True  True]
'''