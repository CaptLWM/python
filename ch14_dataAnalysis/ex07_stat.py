# 통계를 위한 연산
import numpy as np

arr3 = np.arange(5)
print(arr3) # [0 1 2 3 4]
print([arr3.sum(), arr3.mean()]) # [10, 2.0] 합, 몫

print([arr3.min(), arr3.max()]) # [0, 4]
print([arr3.std(), arr3.var()]) # [1.4142135623730951, 2.0] 표준편차, 분산

arr4 = np.arange(1,5)
print(arr4) # [1 2 3 4]
print(arr4.cumsum()) #[ 1  3  6 10] 누적 합
print(arr4.cumprod()) # [ 1  2  6 24] 누적 곱