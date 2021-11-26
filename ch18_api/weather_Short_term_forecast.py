import json
import datetime
import requests

# API_key
API_KEY = 'VbJXaKcK6CP63TcEtzmQ66WNMB1ZbMmjge3s4ckj1AVd85OwQxNvyL%2BnuevKit0PqeWip1X5EvmmUPTTf%2BdACg%3D%3D'
API_KEY_decode = requests.utils.unquote(API_KEY)

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

req_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtFcst"

baseDate = date # 발표 일자
baseTime = time # 발표 시간(정시)

nx_val = 60 # 예보지점 x좌표(종로구 사직동)
ny_val = 127 # 예보지점 y좌표(종로구 사직동)

num_of_rows = 30
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
{'baseDate': '20211126', 'baseTime': '1530',
'category': 'RN1', 'fcstDate': '20211126', 'fcstTime': '1600', 'fcstValue': '1.0mm 미만', 'nx': 60, 'ny': 127},
'''

# 딕셔너리 데이터 분석해서 원하는 값 추출
weather_items = dict_data['response']['body']['items']['item']

sky_cond = ['맑음','','구름 많음','흐림']
rain_type = ['없음','비','비/눈','눈',"",'빗방울','빗방울눈날림','눈날림']

print('[발표날짜:{}]'.format(weather_items[0]['baseDate']))
print('[발표시간:{}]'.format(weather_items[0]['baseTime']))

print('[초단기 일기예보]')
for k in range(len(weather_items)):
    weather_item = weather_items[k]
    fcstTime=weather_item['fcstTime']
    fcstValue=weather_item['fcstValue']

    if(weather_item['category']=='T1H'):
        print("* 시각 : {0}, 기온 : {1} [°C]".format(fcstTime, fcstValue))
    elif(weather_item['category']=='REH'):
        print("* 시각 : {0}, 습도 : {1} [%]".format(fcstTime, fcstValue))
    elif(weather_item['category']=='SKY'):
        print("* 시각 : {0}, 하늘상태 : {1}".format(fcstTime, sky_cond[int(fcstValue)-1]))
    elif(weather_item['category']=='PTY'):
        print("* 시각 : {0}, 강수형태 : {1}".format(fcstTime, rain_type[int(fcstValue)]))
    elif(weather_item['category']=='RN1'):
        print("* 시각 : {0}, 시간당 강수량 : {1} [mm]".format(fcstTime, fcstValue))