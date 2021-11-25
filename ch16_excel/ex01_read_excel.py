# 엑셀 파일의 데이터 읽ㄱ
# df = pd.read_excel()
import pandas as pd
df = pd.read_excel('/Users/iwonmin/Desktop/python/ch16_excel/학생시험성적.xlsx')
print(df)

df = pd.read_excel('/Users/iwonmin/Desktop/python/ch16_excel/학생시험성적.xlsx', sheet_name=1)
print(df)

df = pd.read_excel('/Users/iwonmin/Desktop/python/ch16_excel/학생시험성적.xlsx', sheet_name='2차시험')
print(df)

df = pd.read_excel('/Users/iwonmin/Desktop/python/ch16_excel/학생시험성적.xlsx', sheet_name=1, index_col=0) #인덱스변경
print(df)

df = pd.read_excel('/Users/iwonmin/Desktop/python/ch16_excel/학생시험성적.xlsx', sheet_name=1, index_col='학생') #인덱스변경
print(df)