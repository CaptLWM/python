import pandas as pd

df_A_B = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                      '제품A':[100,150,200,130],
                      '제품B':[90,100,140,170]})
print(df_A_B)
'''
  판매월  제품A  제품B
0  1월  100   90
1  2월  150  100
2  3월  200  140
3  4월  130  170
'''

df_C_D = pd.DataFrame({'판매월':['1월','2월','3월','4월'],
                        '제품':[112, 141, 203,122],
                        '제품D':[90,110,140,170]})
'''
판매월  제품A  제품B   제품  제품D
0  1월  100   90  112   90
1  2월  150  100  141  110
2  3월  200  140  203  140
3  4월  130  170  122  170
'''
                        
print(df_A_B.merge(df_C_D))

df_left = pd.DataFrame({'key':['A','B','C'], 'left':[1,2,3]})
print(df_left)

df_right = pd.DataFrame({'key':['A','B','C'], 'right':[4,5,6]})
print(df_right)

print(df_left.merge(df_right, how='left', on='key'))

print(df_right.merge(df_right, how='outer',on='key'))