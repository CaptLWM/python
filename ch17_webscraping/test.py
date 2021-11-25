import glob
import requests
from bs4 import BeautifulSoup

# billboard hot100 의 곡명과 아티스트를 반환
def billboard_hot100(year, month, day):

    # 월과 일의 경우는 항상 두 자리로 맞춤
    month = "{0:02d}".format(month)
    day = "{0:02d}".format(day)

    base_url = 'https://www.billboard.com/charts/hot-100/'
    url = base_url + '{0}-{1}-{2}'.format(year, month, day)

    html_music = requests.get(url).text
    soup_music = BeautifulSoup(html_music, "lxml")

    titles = soup_music.select('li.lrv-u-width-100p h3')
    artists = soup_music.select('li.lrv-u-width-100p span.u-max-width-330')

    music_titles = [title.get_text() for title in titles]
    music_artists = [artist.get_text().strip() for artist in artists]

    music_titles_list = []
    for i in music_titles:
        mod = i.replace("\n","")
        music_titles_list.append(mod)
    music_artists_list = []
    for i in music_artists:
        mod = i.replace("\n","")
        music_artists_list.append(mod)
    return music_titles_list, music_artists_list


# 날짜를 지정해 builboard_hot100 함수 호출
music_titles_list, music_artists_list = billboard_hot100(2021, 10, 25)

# 곡명과 아티스트를 저장할 파일 이름을 폴더와 함께 지정
file_name = '/Users/iwonmin/Desktop/python/ch17_webscraping/billboard_hot100(211025).txt'

f = open(file_name, 'w', encoding="utf-8")  # 파일 열기

# 추출된 노래 제목과 아티스트를 파일에 저장
for k in range(len(music_titles_list)):
    f.write("{0:3d}:{1}-{2}\n".format(k+1,
                                       music_titles_list[k],  music_artists_list[k]))

f.close()  # 파일 닫기

glob.glob(file_name)  # 생성된 파일 확인

