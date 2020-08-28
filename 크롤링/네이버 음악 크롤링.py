import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
def get_chart_data(chart_name):
	driver = webdriver.Chrome('/usr/local/bin/chromedriver')
	chart_data = []
	for i in range(2):
		url = f"https://music.naver.com/listen/top100.nhn?domain={chart_name}&page={i+1}"
		driver.get(url)
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
				try:
					artist_area = song.find('td',class_='_artist artist')
					artist = artist_area.a['title']
				except:
					artist_area = song.find('td',class_='_artist artist no_ell2')
					artist = artist_area.text.replace('\n','')
				song_data = {"rank":rank,"song_title":title,"artist":artist,"album_img":album_cover}
				chart_data.append(song_data)
			except:
				pass
	driver.close()
	return chart_data
def main():
	total_result = get_chart_data("TOTAL")
	total_df = pd.DataFrame(total_result,columns=["rank","song_title","artist","album_img"])