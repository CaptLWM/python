# 데이터 연산
import pandas as pd

s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([10,20,30,40,50])

s3 = pd.Series([1, 2, 3, 4])
s4 = pd.Series([10, 20, 30, 40, 50])
print(s3 + s4)

table_data1 = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50], 'C': [100, 200, 300, 400,500]}
df1 = pd.DataFrame(table_data1)
print(df1)

table_data2 = {'A': [6, 7, 8],
                'B': [60, 70, 80],
                'C': [600, 700, 800]}
df2 = pd.DataFrame(table_data2)
print(df2)

print(df1 + df2)

table_data3 = {' 봄 ': [256.5, 264.3, 215.9, 223.2, 312.8],
                '여름 ': [770.6, 5, 599.8, 387.1, 446.2],
                '가을 ': [363.5, 231.2, 293.1, 247.7, 381.6],
                '겨울 ': [139.3, 59.9, 76.9, 109.1, 108.1]}
columns_list = [' 봄 ', '여름 ', '가을 ', '겨울']
index_list = ['2012', '2013', '2014', '2015', '2016']
df3 = pd.DataFrame(table_data3, columns=columns_list, index=index_list)
print(df3)

print(df3.mean())

print(df3.mean(axis=1))

print(df3.describe())