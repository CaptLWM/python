import xmltodict
import requests

# 자신의 인증키를 복사해서 입력합니다. / 나중에 내것 발급받으면 내걸로 변경
API_KEY = 'VbJXaKcK6CP63TcEtzmQ66WNMB1ZbMmjge3s4ckj1AVd85OwQxNvyL%2BnuevKit0PqeWip1X5EvmmUPTTf%2BdACg%3D%3D'
API_KEY_decode = requests.utils.unquote(API_KEY)
print(API_KEY_decode)


req_url = "http://openapi.epost.go.kr/postal/retrieveNewAdressAreaCdService/retrieveNewAdressAreaCdService/getNewAddressListAreaCd"

search_Se = "road"
srch_wrd = "가로공원로 136"

req_parameter = {"ServiceKey": API_KEY_decode, #디코딩
                 "searchSe": search_Se, "srchwrd": srch_wrd}

r = requests.get(req_url, params=req_parameter)
xml_data = r.text
print(xml_data)


dict_data = xmltodict.parse(xml_data) #딕셔너리 형태로 변환
print(dict_data)
'''
rderedDict([('NewAddressListResponse', OrderedDict([('cmmMsgHeader', OrderedDict([('requestMsgId', None), ('responseMsgId', None), ('responseTime', '20211126:113950977'), ('successYN', 'Y'), ('returnCode', '00'), ('errMsg', None), ('totalCount', '1'), ('countPerPage', '10'), ('totalPage', '1'), ('currentPage', None)])), ('newAddressListAreaCd', OrderedDict([('zipNo', '06579'), ('lnmAdres', '서울특별시 서초구 반포대로 201 (반포동, 국립중앙도서관)'), ('rnAdres', '서울특별시 서초구 반포동 산60-1 국립중앙도서관')]))]))])
'''


adress_list = dict_data['NewAddressListResponse']['newAddressListAreaCd']
# newAddresListAreaCd : [('zipNo', '06579'), ('lnmAdres', '서울특별시 서초구 반포대로 201 (반포동, 국립중앙도서관)'), ('rnAdres', '서울특별시 서초구 반포동 산60-1 국립중앙도서관')]
print("[입력한 도로명 주소]", srch_wrd)
print("[응답 데이터에서 추출한 결과]")
print("- 우편번호:", adress_list['zipNo'])
print("- 도로명 주소:", adress_list['lnmAdres'])
print("- 지번 주소:", adress_list['rnAdres'])
