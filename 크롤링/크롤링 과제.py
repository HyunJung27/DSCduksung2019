#크롤링 과제
#IMDB에서 영화의 키워드 목록 수집해오는 함수:crawl_movie_keyword 만들어 보기
#영화 코드		영화명
#tt1375666	Inception
#tt1431045	Deadpool
#tt0848228	The Avengers
#tt0468569	The Dark Knight
#tt0816692	Interstellar
#tt0499549	Avatar
#tt2015381	Guardians of the Galaxy
#tt0137523	Fight Club
#tt0371746	Iron Man
#tt1853728	Django Unchained
#url = https://www.imdb.com/title/{영화 코드}/keywords
#url = https://www.imdb.com/title/tt1375666/keywords
#crawl_movie_keyword 함수에 대한 설명

from bs4 import BeautifulSoup
import requests
import time
import re
import pandas as pd
import selenium


def crawl_movie_keyword(imdb_id):
	url = 'https://www.imdb.com/title/{imbd_id_list}/keywords'
    req = requests.get(url)
    html = req.text
    bs = BeautifulSoup(url, 'html.parser')
    bs.find(id = 'imbd_id_list')
    bs.find_all('a')[0].get_text()
    table = bs.find('table', class_='fixed')
    tbody = table.tbody
    body = str(tbody.get_text())

    for i in bs.find()

	imbd_id_list = ["tt1375666", "tt1431045", "tt0848228","tt0468569","tt0816692","tt0499549","tt2015381","tt0137523","tt1853728"]
    result = []

