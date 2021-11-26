import requests

# API_key
API_KEY = 'VbJXaKcK6CP63TcEtzmQ66WNMB1ZbMmjge3s4ckj1AVd85OwQxNvyL%2BnuevKit0PqeWip1X5EvmmUPTTf%2BdACg%3D%3D'
API_KEY_decode = requests.utils.unquote(API_KEY)


import json
import datetime

# 날짜 및 시간 설정
now = datetime.datetime.now()

# baseDate에 날짜를 입력하기 위해 날짜를 출력형식을 지정해 변수에 할당
date = "{:%Y%m%d}".format(now)

# baseTime에 시간(정시)를 입력하기 위해 출력 형식을 지정해 시간변수만 변수에 할당
time = "{:%H00}".format(now)

# 현재 분의 30분 이전이면 이전시간(정시)을 설정
if(now.minute >= 30):
    time="{0}00".format(now.hour)
else :
    time="{0}00".format(now.hour-1)

# 요청 주소 및 요청 변수 지정

req_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst"

baseDate = date # 발표 일자
baseTime = time # 발표 시간(정시)

nx_val = 60 # 예보지점 x좌표(종로구 사직동)
ny_val = 127 # 예보지점 y좌표(종로구 사직동)

num_of_rows = 6
page_no = 1

output_type = 'JSON'

req_parameter = {"ServiceKey":API_KEY_decode,
                "nx":nx_val, "ny":ny_val,
                "base_date":baseDate,"base_time":baseTime,
                "pageNo":page_no, "numOfRows":num_of_rows,
                "dataType":output_type}

# 데이터 요청
r = requests.get(req_url, params = req_parameter)

dict_data = r.json()
print(dict_data)

'''
{'response': {'header': {'resultCode': '00', 'resultMsg': 'NORMAL_SERVICE'},
 'body': {'dataType': 'JSON',
    'items': {'item': [{'baseDate': '20211126',
        'baseTime': '1400',
        'category': 'TMP',
        'fcstDate': '20211126',// 예보일자
        'fcstTime': '1500', // 예보시간
        'fcstValue': '6',
        'nx': 60, 'ny': 127}, 
        {'baseDate': '20211126',
        'baseTime': '1400',
        'category': 'UUU',
        'fcstDate': '20211126',
        'fcstTime': '1500',
        'fcstValue': '2.2',
        'nx': 60, 'ny': 127}, {'baseDate': '20211126', 'baseTime': '1400', 'category': 'VVV', 'fcstDate': '20211126', 'fcstTime': '1500', 'fcstValue': '-1.5', 'nx': 60, 'ny': 127}, {'baseDate': '20211126', 'baseTime': '1400', 'category': 'VEC', 'fcstDate': '20211126', 'fcstTime': '1500', 'fcstValue': '304', 'nx': 60, 'ny': 127}, {'baseDate': '20211126', 'baseTime': '1400', 'category': 'WSD', 'fcstDate': '20211126', 'fcstTime': '1500', 'fcstValue': '2.7', 'nx': 60, 'ny': 127}, {'baseDate': '20211126', 'baseTime': '1400', 'category': 'SKY', 'fcstDate': '20211126', 'fcstTime': '1500', 'fcstValue': '3', 'nx': 60, 'ny': 127}]}, 'pageNo': 1, 'numOfRows': 6, 'totalCount': 700}}}
'''

# 딕셔너리 데이터 분석해서 원하는 값 추출
weather_items = dict_data['response']['body']['items']['item']

print('[발표날짜:{}]'.format(weather_items[0]['baseDate']))
print('[발표시간:{}]'.format(weather_items[0]['baseTime']))

for k in range(len(weather_items)):
    weather_item = weather_items[k]
    obsrValue = weather_item['obsrValue']
    if(weather_item['category']=='T1H'):
        print("* 기온 : {} [°C]".format(obsrValue))
    elif(weather_item['category']=='REH'):
        print("* 습도 : {} [%]".format(obsrValue))
    elif(weather_item['category']=='RN1'):
        print("* 1시간 강수량 : {} [mm]".format(obsrValue))
        