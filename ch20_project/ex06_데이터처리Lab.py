# 1. 수집된 데이터 파일의 구조 분석
from datetime import datetime
import os
import pandas as pd
import glob
data_file = '/Users/iwonmin/Desktop/python/ch20_project/seoul_expense/2017/201701_expense_list.csv'

# 파일 구조 파악
with open(data_file, encoding='utf-8') as f:
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()

    # print(line1)
    # print(line2)
    # print(line3)
'''
nid,title,url,dept_nm_lvl_1,dept_nm_lvl_2,dept_nm_lvl_3,dept_nm_lvl_4,dept_nm_lvl_5,exec_yr,exec_month,
expense_budget,expense_execution,category,dept_nm_full,exec_dt,exec_loc,exec_purpose,target_nm,payment_method,exec_amount

11430252,"2017년 1월 장애인복지정책과 업무추진비 집행내역",http://opengov.seoul.go.kr/public/11430252,서
울시본청,복지본부,장애인복지정책과,,,2017,1,,,,"복지본부 장애인복지정책과","2017-01-26 13:10","동해일식 
(중구 무교동)","기본소득과 장애인복지 논의간담회","장애인복지정책팀장 외 2명",카드,76000

11430252,"2017년 1월 장애인복지정책과 업무추진비 집행내역",http://opengov.seoul.go.kr/public/11430252,서
울시본청,복지본부,장애인복지정책과,,,2017,1,,,,"복지본부 장애인복지정책과","2017-01-25 22:41","김앤장 ( 
중구 무교로)","장애인단체 활동지원 논의간담회","장애인복지정책과장 외 3명",카드,102000

'''

line1_len = len(line1.split(','))
line2_len = len(line2.split(','))
line3_len = len(line3.split(','))

#print("[각 줄의 데이터값의 개수]")
#print("첫째 줄:{}, 둘째 줄:{}, 셋째 줄:{}".format(line1_len, line2_len, line3_len))
'''
[각 줄의 데이터값의 개수]
첫째 줄:20, 둘째 줄:20, 셋째 줄:20
'''

# 비용, 내역, 참석자
# 250,000, "시장 격려금", 시장 /3갠데 4개로 인식 될 수 있음
# 250000, "시장, 시의원 조찬", 시장 /3갠데 4개로 인식 될 수 있음
# 250000, "시장, 시의원 조찬", 시장,"내용1,내용2" 

def get_value_count(line):

    line_rep_list = [] #[250000, "시장, 시의원 조찬", 시장,"내용1,내용2" ]
    for k, x in enumerate(line.split('"')):
        if(k % 2 != 0):
            x = x.replace(',', '') # , 를 공백으로 변경
        line_rep_list.append(x)

    #print("****")
    #print(line_rep_list)
    line_rep_str = ''.join(line_rep_list) # 250000, "시장 시의원 조찬", 시장, "내용1 내용2" 
    print(line_rep_str)

    return len(line_rep_str.split(','))


line1_len = get_value_count(line1)
line2_len = get_value_count(line2)
line3_len = get_value_count(line3)

print("[각 줄의 데이터값의 개수]")
print("첫째 줄:{}, 둘째 줄:{}, 셋째 줄:{}".format(line1_len, line2_len, line3_len))
'''
[각 줄의 데이터값의 개수]
첫째 줄:20, 둘째 줄:20, 셋째 줄:20
'''

# 2. 첫 번째 줄의 열 이름과 개수 변경
def change_csv_file_first_line_value(old_file_name, new_file_name):
    with open(old_file_name, encoding='utf-8') as f:  # 파일을 읽기 모드로 열기
        # 전체 데이터를 읽어서 한 줄씩 lines 리스트의 각 요소에 할당
        lines = f.read().splitlines() # ['첫번째줄','두번째줄','세번째줄']

    # 첫째 줄의 내용을 변경할 열 이름을 지정해서 변경
    lines[0] = 'nid,제목,url,부서레벨1,부서레벨2,부서레벨3,부서레벨4,부서레벨5,\
집행연도,집행월,예산,집행,구분,부서명,집행일시,집행장소,집행목적,대상인원,결제방법,집행금액'

    with open(new_file_name, 'w', encoding='utf-8') as f:  # 파일을 쓰기 모드로 열기
        # 리스트 내의 각 요소를 개행문자(\n)로 연결해서 파일로 저장
        f.write('\n'.join(lines)) # '첫번째줄\n두번째줄\n세번째줄\n'


# 기존의 파일
old_file_name = '/Users/iwonmin/Desktop/python/ch20_project/seoul_expense/2017/201701_expense_list.csv'

# 새로운 파일
new_file_name = '/Users/iwonmin/Desktop/python/ch20_project/seoul_expense/2017/201701_expense_list_new.csv'

# 첫째 줄의 내용을 변경한 새로운 파일 생성
change_csv_file_first_line_value(old_file_name, new_file_name)


with open(new_file_name, encoding='utf-8') as f:  # 파일을 읽기 모드로 열기
    for k in range(3):
        print(f.readline())

# 인자: 연도, 데이터 파일이 있는 폴더
def change_year_csv_file_first_line_value(year, data_folder):

    # 데이터 파일이 있는 폴더 지정
    # ex) 'C:/myPyCode/data/seoul_expense/2017/'
    expense_list_year_dir = data_folder + str(year) + '/'

    extension = 'csv'  # 확장자 이름

    # 지정한 폴더에 있는 월별 업무추진비 파일에서 첫 번째 줄의 열 이름을 변경
    for k in range(12):
        # 기존의 파일 이름 지정
        old_file_name = expense_list_year_dir + \
            '{0}{1:02d}_expense_list.{2}'.format(year, k+1, extension)

        # 새로운 파일 이름 지정
        new_file_name = expense_list_year_dir + \
            '{0}{1:02d}_expense_list_new.{2}'.format(year, k+1, extension)

        # 첫째 줄의 내용을 변경한 새로운 파일 생성
        change_csv_file_first_line_value(old_file_name, new_file_name)


data_folder = '/Users/iwonmin/Desktop/python/ch20_project/seoul_expense/'

years = [2017, 2018, 2019, 2020, 2021]  # 연도를 지정

for year in years:
    print("{}년 데이터의 첫 번째 줄의 열 이름을 변경해서 새 파일에 저장합니다.".format(year))
    change_year_csv_file_first_line_value(year, data_folder)

print("모든 데이터의 첫 번째 줄의 열 이름을 변경해서 새 파일로 저장했습니다.")