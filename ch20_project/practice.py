# 데이터 분석
from wordcloud import WordCloud
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

data_folder = '/Users/iwonmin/Desktop/python/ch20_project/seoul_expense/'
years = [2017, 2018, 2019]

df_expense_all = pd.DataFrame()

for year in years:
    expense_list_year_dir = data_folder + str(year) + '/'
    expense_list_tidy_file = "{}_expense_list_tidy.csv".format(year)

    path_file_name = expense_list_year_dir + expense_list_tidy_file

    df_expense = pd.read_csv(path_file_name)
    df_expense_all = df_expense_all.append(df_expense, ignore_index=True)


#print(df_expense_all.info())
'''
<class 'pandas.core.frame.DataFrame'>  
RangeIndex: 216557 entries, 0 to 216556
Data columns (total 12 columns):       
 #   Column  Non-Null Count   Dtype
---  ------  --------------   -----
 0   제목      216557 non-null  object
 1   부서레벨1   216557 non-null  object
 2   부서레벨2   216273 non-null  object
 3   집행연도    216557 non-null  int64
 4   집행월     216557 non-null  int64
 5   부서명     216478 non-null  object
 6   집행일시    216557 non-null  object
 7   집행장소    214401 non-null  object
 8   집행목적    216535 non-null  object
 9   대상인원    215535 non-null  object
 10  결제방법    216354 non-null  object
 11  집행금액    216557 non-null  int64
dtypes: int64(3), object(9)
memory usage: 19.8+ MB
None
'''

#print(df_expense_all.head(2))
'''
                             제목  부서레벨1 부서레벨2  집행연도  ...               집행목적            대상 
인원 결제방법    집행금액
0  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017  ...  기본소득과 장애인복지 논
의간담회  장애인복지정책팀장 외 2명   카드   76000
1  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017  ...   장애인단체 활동지원 논 
의간담회  장애인복지정책과장 외 3명   카드  102000

[2 rows x 12 columns]
'''

#print(df_expense_all.tail(2))
'''
                                                제목 부서레벨1    부서레벨2  ...       대상인원  결제방법    
집행금액
216555  2019년 12월 사업소 서울시립대학교 중앙도서관 사서과 업무추진비 - 전체   사업소  서울시립대학교  ...  
사서과장 외 8명    카드  23940
216556  2019년 12월 사업소 서울시립대학교 중앙도서관 사서과 업무추진비 - 전체   사업소  서울시립대학교  ...  
  이용자 80명    카드  53420

[2 rows x 12 columns]
'''

matplotlib.rcParams['font.family'] = 'AppleGothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 요일별 및 시간대별 분석
df_expense_all['집행일시'].values
expense_date_time = pd.to_datetime(df_expense_all['집행일시'])
print(expense_date_time.values)
'''
['2017-01-26T13:10:00.000000000' '2017-01-25T22:41:00.000000000'
 '2017-01-24T12:35:00.000000000' ... '2019-12-19T11:34:00.000000000'
 '2019-12-16T12:39:00.000000000' '2019-12-03T17:35:00.000000000']
'''

week_day_name=['월','화','수','목','금','토','일']
df_expense_all['집행일시_요일']=[week_day_name[weekday] for weekday in expense_date_time.dt.weekday]
df_expense_all['집행일시_시간'] = [hour for hour in expense_date_time.dt.hour]

print(df_expense_all.head(3))

'''
                            제목  부서레벨1 부서레벨2  집행연도  집행월  ...            대상인원 결제방법    집행금액 집행일시_요일 집행일시_시간
0  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017    1  ...  장애인복지정책팀장 외 2명   카드   76000       목      13
1  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017    1  ...  장애인복지정책과장 외 3명   카드  102000       수      22
2  2017년 1월 장애인복지정책과 업무추진비 집행내역  서울시본청  복지본부  2017    1  ...    장애인복지정책팀장외7명   카드   80000       화      12
'''
expense_weekday = df_expense_all['집행일시_요일'].value_counts()
print(expense_weekday)
'''
[3 rows x 14 columns]
목    45683
화    43812
수    42343
금    41381
월    39498
토     2238
일     1602
Name: 집행일시_요일, dtype: int64
'''

expense_weekday = expense_weekday.reindex(index = week_day_name)
print(expense_weekday)
'''
월    39498
화    43812
수    42343
목    45683
금    41381
토     2238
일     1602
Name: 집행일시_요일, dtype: int64
'''

expense_weekday.plot.bar(rot=0)
plt.title("요일별 업무추진비 집행 횟수")
plt.xlabel("요일")
plt.ylabel("집행횟수")
plt.show()

expense_hour_num = df_expense_all['집행일시_시간'].value_counts()
print(expense_hour_num)
'''
12    87518
20    23013
13    20990
19    16766
21    12210
11     8356
14     8311
15     7168
10     5824
18     5783
16     5169
0      4919
9      3486
17     2889
22     2563
8       875
7       412
23      128
1        44
6        42
3        27
4        26
5        19
2        19
Name: 집행일시_시간, dtype: int64
'''

work_hour=[(k+8)%24 for k in range(24)]
expense_hour_num = expense_hour_num.reindex(index = work_hour)
print(expense_hour_num)
'''
8       875
9      3486
10     5824
11     8356
12    87518
13    20990
14     8311
15     7168
16     5169
17     2889
18     5783
19    16766
20    23013
21    12210
22     2563
23      128
0      4919
1        44
2        19
3        27
4        26
5        19
6        42
7       412
Name: 집행일시_시간, dtype: int64
'''

expense_hour_num.plot.bar(rot=0)
plt.title('시간별 업무추진비 집행 횟수')
plt.xlabel('집행시간')
plt.ylabel('집행횟수')
plt.show()

expense_hour_total = pd.pivot_table(df_expense_all, index = ['집행일시_시간'], values=['집행금액'], aggfunc = sum)
print(expense_hour_total.head())
'''
              집행금액
집행일시_시간           
0        842523116
1          7024161
2          2265190
3          7215762
4          5818431
'''

eok_won = 100000000 #억원
expense_hour_total = expense_hour_total.reindex(index = work_hour)

(expense_hour_total/eok_won).plot.bar(rot=0)
plt.ylabel('집행금액(억원)')
plt.title('시간대별 업무추진비 집행 금액')
plt.show()