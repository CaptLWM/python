# 데이터 수집
import glob
import requests
import os
import pathlib

#인자: 확장자, 연도, 내려받을 폴더


def get_seoul_expense_list(extension, year, data_folder):

    # 깃허브의 데이터 위치 지정
    # ex) 'https://github.com/seoul-opengov/opengov/raw/master/expense_list2017/'
    expense_list_year_url = 'https://github.com/seoul-opengov/opengov/raw/master/expense_list' + \
        str(year) + '/'

    # 데이터를 내려받을 폴더 지정
    # ex) 'C:/myPyCode/data/seoul_expense/2017/'
    expense_list_year_dir = data_folder + str(year) + '/'

    # 내려받을 폴더가 없다면 폴더 생성
    if(os.path.isdir(expense_list_year_dir)):
        print("데이터 폴더({0})가 이미 있습니다. {0}년 데이터의 다운로드를 시작합니다.".format(year))
    else:
        print("데이터 폴더({0})가 없어서 생성했습니다. {0}년 데이터의 다운로드를 시작합니다.".format(year))
        # 폴더 생성
        pathlib.Path(expense_list_year_dir).mkdir(parents=True, exist_ok=True)

    # 지정한 폴더로 1월 ~ 12월 업무추진비 파일을 다운로드
    for k in range(12):
        file_name = '{0}{1:02d}_expense_list.{2}'.format(year, k+1, extension)
        url = expense_list_year_url + file_name
        print(url)
        r = requests.get(url)
        with open(expense_list_year_dir + file_name, 'wb') as f:
            f.write(r.content)


# 내려받을 업무추진비 데이터의 파일 형식을 지정
extension = "csv"

data_folder = '/Users/iwonmin/Desktop/python/ch20_project/seoul_expense/'

years = [2017, 2018, 2019,2020,2021]  # 다운로드받을 연도를 지정

extension = "csv"
# extension = "xlsx"
# extension = "xml"

for year in years:
    get_seoul_expense_list(extension, year, data_folder)

print("모든 데이터를 다운로드 받았습니다.")


data_folder = '/Users/iwonmin/Desktop/python/ch20_project/seoul_expense/'

years = [2017, 2018, 2019,2020, 2021]  # 다운로드받을 연도를 지정

for year in years: # 파일 다운로드 확인
    path_name = data_folder + str(year) + "/"  # 연도별 폴더명을 지정

    # 지정 폴더에서 파일명에 list.csv가 포함된 파일만 지정
    file_name_for_glob = path_name + "*list.csv"

    csv_files = []
    for csv_file in glob.glob(file_name_for_glob):
        # 반환값에서 폴더는 제거하고 파일명만 추출
        csv_files.append(csv_file.split("\\")[-1])

    print("[폴더 이름]", path_name)  # 폴더명 출력
    print("* CSV 파일:", csv_files)