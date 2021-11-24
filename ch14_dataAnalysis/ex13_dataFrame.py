# DataFrame을 활용한 데이터 생성
# DataFrame : pandas에서는 표(table)와 같은 2차원 데이터 처리하기 위한 자료구조

import numpy as np
import pandas as pd

print(pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]]))
'''
   0  1  2
0  1  2  3
1  4  5  6
2  7  8  9
'''

data_list = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(data_list)
'''
[[10 20 30]
 [40 50 60]
 [70 80 90]]
'''

print(pd.DataFrame(data_list))
'''
    0   1   2
0  10  20  30
1  40  50  60
2  70  80  90
'''

data = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
index_date = pd.date_range('2019-01-01', periods=4)
columns_list = ['A','B','C']
print(pd.DataFrame(data, index=index_date, columns=columns_list))
'''
             A   B   C
2019-01-01   1   2   3
2019-01-02   4   5   6
2019-01-03   7   8   9
2019-01-04  10  11  12
'''

table_data = {'연도': [2015, 2016, 2016, 2017, 2018],
              '지사': ['한국','한국','미국','영국','일본'],
              '고객 수' : [200,250,400,500,201]}
print(table_data) # 딕셔너리
# {'연도': [2015, 2016, 2016, 2017, 2018], '지사': ['한국', '한국', '미국', '영국', '일본'], '고객 수': [200, 250, 400, 500, 201]}

print(pd.DataFrame(table_data))
'''
     연도  지사  고객 수
0  2015  한국   200
1  2016  한국   250
2  2016  미국   400
3  2017  영국   500
4  2018  일본   201
'''

df = pd.DataFrame(table_data, columns=['연도','지사']) # 해당 칼럼만 호출
print(df)
'''
     연도  지사
0  2015  한국
1  2016  한국
2  2016  미국
3  2017  영국
4  2018  일본
'''

print(df.index) # RangeIndex(start=0, stop=5, step=1) / index 호출
print(df.columns) # Index(['연도', '지사'], dtype='object') / columns 호출
print(df.values)
'''
[[2015 '한국']
 [2016 '한국']
 [2016 '미국']
 [2017 '영국']
 [2018 '일본']]
'''