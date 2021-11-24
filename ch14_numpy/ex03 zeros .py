# 특별한 형태의 배열 생성
import numpy as np

# np.zeros()함수는 모든 원소가 0으로 배열을 만든다.
print(np.zeros(10))
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

print(np.zeros((3,4)))
'''
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]
'''

print(np.ones(5))
# [1. 1. 1. 1. 1.]

print(np.ones((3,5)))
'''
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
'''

# np.eye(n) 함수 nxn 단위행렬(identify matrix, 항등행렬). A x I = A
print(np.eye(3))
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''

