# 행렬 연산
import numpy as np

A = np.array([0, 1, 2, 3]).reshape(2,2) # 1차원을 2차원으로
print(A)

B = np.array([3,2,1,0]).reshape(2,2)
print(B)

# A x B
print(A.dot(B))
'''
[[1 0]
 [9 4]]
'''

print(np.dot(A,B))

# A의 전치행렬
print(np.transpose(A))
print(A.transpose())

# 행렬 A의 역행렬
print(np.linalg.inv(A))
print(np.linalg.det(A)) #-2.0 / 행렬식 구하는 함수, 0이면 역행렬이 없음
