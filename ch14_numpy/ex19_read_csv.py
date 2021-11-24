import pandas as pd

print(pd.read_csv('/Users/iwonmin/Desktop/python/ch14_numpy/sea_rain1.csv')) # 맥이랑 윈도우 저장경로 다르므로 주의할것
'''
     연도       동해       남해       서해       전체
0  1996  17.4629  17.2288  14.4360  15.9067
1  1997  17.4116  17.4092  14.8248  16.1526
2  1998  17.5944  18.0110  15.2512  16.6044
3  1999  18.1495  18.3175  14.8979  16.6284
4  2000  17.9288  18.1766  15.0504  16.6178
'''

print(pd.read_csv('/Users/iwonmin/Desktop/python/ch14_numpy/sea_rain1.csv', index_col="연도")) # 맥이랑 윈도우 저장경로 다르므로 주의할것
'''
          동해       남해       서해       전체
연도
1996  17.4629  17.2288  14.4360  15.9067
1997  17.4116  17.4092  14.8248  16.1526
1998  17.5944  18.0110  15.2512  16.6044
1999  18.1495  18.3175  14.8979  16.6284
2000  17.9288  18.1766  15.0504  16.6178
'''
