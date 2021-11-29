import requests
# 깃허브의 파일 URL
url = 'https://github.com/wikibook/python-for-data-analysis-rev/raw/master/readme.txt'
# URL 에 해당하는 파일을 내려받음
r = requests.get(url)
print(r.text)
# 파일을 저장할 폴더와 파일명을 지정
file_name = '/Users/iwonmin/Desktop/python/ch20_project/readme.txt'
# 내려받은 파일을 지정한 폴더에 저장
with open(file_name, 'wb') as f:
    f.write( r.content)