# 웹페이지의 HTML 소스 갖고 오기

import requests

r = requests.get("https://google.com")
print(r)
# <Response [200]>

print(r.text[0:100])
# <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content

html = requests.get('https://google.com').text
print(html[0:100])
# <!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content