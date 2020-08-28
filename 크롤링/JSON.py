# 연습 - 종합 2007년 전체 데이터 가져오기
# 받는 값 : (total, domestic, oversea) , year
# 월, 주는 반복문 돌리기 , try문 사용할 것
# 한계 : 2020년 1월 1주 데이터를 긁어올 수 없음
def music_history(kind , year):
    chart_data = []
    driver = webdriver.Chrome("/Users/mycelebs_temp/chromedriver")
    for i in range(12): # month
        for week in range(6): # week
            for p in range(2):  # page
                if i < 9:
                    url = f"https://music.naver.com/listen/history/index.nhn?type={kind}&year={year}&month=0{i+1}&week={week}&page={p+1}"
                else :
                    url = f"https://music.naver.com/listen/history/index.nhn?type={kind}&year={year}&month={i+1}&week={week}&page={p+1}"
                driver.get(url)
                time.sleep(1)
                test = driver.find_element_by_xpath('//*[@id="content"]/div[3]/div[1]/span').text
                if test != "2020.01.06~2020.01.12까지 히스토리입니다.":
                    html = driver.page_source
                    soup = BeautifulSoup(html,"html.parser")
                    chart = soup.find('tbody')
                    songs = chart.find_all("tr")
                    for song in songs:
                        try:
                            rank = int(song.find('td',class_='ranking').text)
                            name_area = song.find('td',class_="name")
                            album_cover = name_area.a["href"]
                            title = name_area.find('span',class_='ellipsis').text
                            if week == 0:
                                date = (year + '년 '+ str(i+1) +'월 전체')
                            else:
                                date = (year + '년 ' + str(i+1) + '월 ' + str(week) +'주')
                            #print(date)
                            try:
                                artist_area = song.find('td',class_='_artist artist')
                                artist = artist_area.a['title']
                            except:
                                artist_area = song.find('td',class_='_artist artist no_ell2')
                                artist = artist_area.text.replace('\n','')
                            song_data = {"date":date,"rank":rank,"song_title":title,"artist":artist,"album_img":album_cover}
                            chart_data.append(song_data)
                        except:
                            pass
                else :
                    pass
    total_df = pd.DataFrame(chart_data,columns=["date","rank","song_title","artist","album_img"])
    total_df = total_df.set_index('date')
    if kind == ("TOTAL" or "DOMESTIC"):
        total_df.to_csv( kind+'_'+ year + ".csv" , encoding = 'cp949')
    else :
        total_df.to_csv( kind+'_'+ year + ".csv" , encoding = 'utf-8')
    driver.close()