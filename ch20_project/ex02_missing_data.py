# 결측치 처리
import pandas as pd
data_file = "/Users/iwonmin/Desktop/python/ch20_project/missing_data_test.csv"

df = pd.read_csv(data_file, encoding='cp949', index_col='연도')
# print(df)
'''
        제품1  제품2    제품3    제품4
연도                            
2015  250.0  150    NaN    NaN
2016  200.0  160  170.0    NaN
2017  150.0  200  100.0  150.0
2018  120.0  230  130.0  170.0
2019    NaN  250  140.0    NaN
'''

# print(df.isnull()) # NaN 값을 True
'''
        제품1    제품2    제품3    제품4
연도                              
2015  False  False   True   True
2016  False  False  False   True
2017  False  False  False  False
2018  False  False  False  False
2019   True  False  False   True
'''

# print(df.isnull().sum()) #True 개수
'''
제품1    1
제품2    0
제품3    1
제품4    3
dtype: int64
'''

# 결측치 처리
# print(df.drop(index=[2019])) #index가 2019인 항목 삭제
'''
        제품1  제품2    제품3    제품4
연도                            
2015  250.0  150    NaN    NaN
2016  200.0  160  170.0    NaN
2017  150.0  200  100.0  150.0
2018  120.0  230  130.0  170.0
'''

# print(df.drop(columns=['제품3','제품4'])) #column이 제품3,제품4 제거
'''
        제품1  제품2
연도              
2015  250.0  150
2016  200.0  160
2017  150.0  200
2018  120.0  230
2019    NaN  250
'''

# print(df.drop(index=[2019], columns=['제품3','제품4'])) # index와 columns 동시에 지정 가능
'''
        제품1  제품2
연도              
2015  250.0  150
2016  200.0  160
2017  150.0  200
2018  120.0  230
'''

# print(df.dropna()) # Nan 없는 부분 출력
# print(df.dropna(axis=0)) # axis=0 : 결측치 있는 행 / axis=1 : 결측치 있는 열
'''
        제품1  제품2    제품3    제품4
연도                            
2017  150.0  200  100.0  150.0
2018  120.0  230  130.0  170.0
'''

#print(df.dropna(axis=1)) # axis=1 : 결측치 있는 열
'''
     제품2
연도       
2015  150
2016  160
2017  200
2018  230
2019  250
'''

# print(df.dropna(axis=1, subset=[2015])) #index가 2015인 행에서 결측치 있는 열 제거
'''
        제품1  제품2
연도              
2015  250.0  150
2016  200.0  160
2017  150.0  200
2018  120.0  230
2019    NaN  250
'''

# print(df.fillna(0)) # NaN에 0으로 체움
'''
        제품1  제품2    제품3    제품4
연도                            
2015  250.0  150    0.0    0.0
2016  200.0  160  170.0    0.0
2017  150.0  200  100.0  150.0
2018  120.0  230  130.0  170.0
2019    0.0  250  140.0    0.0
'''

print(df.fillna(method='bfill'))
print(df.fillna(method='bfill').fillna(method='ffill'))

values = {'제품1':100, '제품4':400}
print(df.fillna(value=values))
