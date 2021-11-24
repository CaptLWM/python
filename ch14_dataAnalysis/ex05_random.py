# 난수 배열의 생성
import numpy as np

print(np.random.rand()) # 0.22212502210670226
print(np.random.rand(2,3))
'''
[[0.35941222 0.19643836 0.92235121]
 [0.8394341  0.44277789 0.52803653]]
'''

print(np.random.rand(2,3,4)) # 행렬 2개 3x4행렬로
'''
[[[0.0062434  0.16216849 0.0469312  0.35204625]
  [0.73033044 0.65992464 0.14487388 0.00431128]
  [0.40496432 0.52794684 0.55150352 0.74188428]]

 [[0.51544764 0.42300156 0.72063119 0.58776028]
  [0.19471542 0.49217366 0.97347834 0.93305174]
  [0.92568112 0.59933026 0.87031116 0.27241476]]]
'''

print(np.random.randint(10, size=(3,4))) # 범위, 행렬사이즈
'''
[[7 0 6 0]
 [4 9 7 8]
 [2 1 3 1]]
'''