# 날짜 자동 생성 : date_range
# pd.date_range(start_None, end=None, periods=None, feq='D')
import pandas as pd

print(pd.date_range(start='2019-01-01', end='2019-01-07'))
'''
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07'],
              dtype='datetime64[ns]', freq='D')
'''

print(pd.date_range(start='2019/01/01', end='2019/01/07')) # 결과 똑같음
'''
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07'],
              dtype='datetime64[ns]', freq='D')
'''

print(pd.date_range(start='2019-01-01', periods=7)) # 시작일부터 7일
'''
DatetimeIndex(['2019-01-01', '2019-01-02', '2019-01-03', '2019-01-04',
               '2019-01-05', '2019-01-06', '2019-01-07'],
              dtype='datetime64[ns]', freq='D')
'''

print(pd.date_range(start='2019-01-01', periods=4, freq='2D')) # 2일 간격으로 4일
# DatetimeIndex(['2019-01-01', '2019-01-03', '2019-01-05', '2019-01-07'], dtype='datetime64[ns]', freq='2D')

print(pd.date_range(start='2019-01-01', periods=4, freq='2W')) # 2주 간격으로 4일
# DatetimeIndex(['2019-01-06', '2019-01-20', '2019-02-03', '2019-02-17'], dtype='datetime64[ns]', freq='2W-SUN')

print(pd.date_range(start='2019-01-01', periods=12, freq='2BM')) # 각 달의 마지막날 기준으로 2달 간격으로 12일
'''
DatetimeIndex(['2019-01-31', '2019-03-29', '2019-05-31', '2019-07-31',
               '2019-09-30', '2019-11-29', '2020-01-31', '2020-03-31',
               '2020-05-29', '2020-07-31', '2020-09-30', '2020-11-30'],
              dtype='datetime64[ns]', freq='2BM')
'''

print(pd.date_range(start='2019-01-01', periods=4, freq='QS')) # 분기별 4일
# DatetimeIndex(['2019-01-01', '2019-04-01', '2019-07-01', '2019-10-01'], dtype='datetime64[ns]', freq='QS-JAN')

print(pd.date_range(start='2019-01-01', periods=4, freq='AS')) # 년별 4일
# DatetimeIndex(['2019-01-01', '2020-01-01', '2021-01-01', '2022-01-01'], dtype='datetime64[ns]', freq='AS-JAN')

print(pd.date_range(start='2019-01-01 08:00', periods=10, freq='H')) # 시간간격으로 10개
'''
DatetimeIndex(['2019-01-01 08:00:00', '2019-01-01 09:00:00',
               '2019-01-01 10:00:00', '2019-01-01 11:00:00',
               '2019-01-01 12:00:00', '2019-01-01 13:00:00',
               '2019-01-01 14:00:00', '2019-01-01 15:00:00',
               '2019-01-01 16:00:00', '2019-01-01 17:00:00'],
              dtype='datetime64[ns]', freq='H')
'''

print(pd.date_range(start='2019-01-01 08:00', periods=4, freq='30min'))