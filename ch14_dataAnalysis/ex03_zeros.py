import numpy as np

print(np.zeros(10))
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
print(np.ones(5))
'''
[1. 1. 1. 1. 1.]
'''
print(np.ones((3,5)))
'''
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
'''

# np.eye(n) 함수 nxn 단위행렬(identify matrix, 항등행렬)
print(np.eye(3))
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''