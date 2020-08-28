#차트 히스토리 07년부터 2019년까지 긁어오기
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import time
import os
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
def get_chart_data():
    chart_data = []
    for n in range(2):
        url = 'https://music.naver.com/listen/history/index.nhn?type='+str(list[x])+'&year=' + str(i) + '&month=' + str(k).zfill(2) + '&week=' + str(m) + '&page=' + str(n+1) + ''
        driver.get(url)
        # time.sleep(1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        chart = soup.find('tbody')
        songs = chart.find_all('tr')
        match_select = soup.find('div', class_='section_tit')
        match_text = match_select.find('span', class_='dsc').text
        match_detail = match_text.split('.')
        month = str(k).zfill(2)
        if str(i) == match_detail[0] and month == match_detail[1]:
            for song in songs:
                try:
                    rank = song.find('td', class_='ranking').text
                    name_area = song.find('td', class_='name')
                    img_url = name_area.a['href']
                    song_name = name_area.find('span', class_='ellipsis').text
                    try:
                        artist_area = song.find('td', class_='_artist artist')
                        artist_name = artist_area.a['title']
                    except:
                        artist_area = song.find('td', class_='_artist artist no_ell2')
                        artist_name = artist_area.text.replace('\n', '')
                    song_data = {'rank': rank, 'song_name': song_name, 'artist_name': artist_name,'img_url': img_url}
                    chart_data.append(song_data)
                except:
                    pass
        else:
            song_data = {'rank': None, 'song_name': None, 'artist_name': None, 'img_url': None}
            chart_data.append(song_data)
    return chart_data
list = ['TOTAL', 'DOMESTIC', 'OVERSEA', ['종합', '국내', '해외']]
for x in range(len(list)-1):
    for i in range(2007, 2020):
        os.mkdir(f'/Users/mycelebs_it/PycharmProjects/crawling_class/chart_history/{list[3][x]}/{str(i)}/')
        for k in range(1, 13):
            for m in range(0, 6):
                if i == 2010 and k == 6 and m == 2:
                    m = m + 1
                result = get_chart_data()
                result_df = pd.DataFrame(result, columns=['rank', 'song_name', 'artist_name', 'img_url']).reset_index(drop=True)
                if result_df.loc[0, 'rank'] != None:
                    file = str(list[3][x]) + ' ' +str(i)+'년 '+ str(k).zfill(2) + '월 ' + str(m) +'주차 차트'
                    # result_df.to_excel('./{}/{}/{}.xlsx'.format(list[3][x], str(i) ,file), encoding='utf8')
                    result_df.to_excel(f'/Users/mycelebs_it/PycharmProjects/crawling_class/chart_history/{list[3][x]}/{str(i)}/{file}.xlsx', encoding='utf8')
                else:
                    pass
print('finish')
driver.close()