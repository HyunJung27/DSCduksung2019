#xpath를 이용한 크롤링
import pandas as pd
from selenium import webdriver
from tqdm import tqdm
import time
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.implicitly_wait(3)
#driver.get('https://music.naver.com/listen/top100.nhn?domain=TOTAL&page=1')
#url = driver.current_url
def crwaling(m):
    for k in range(2):
        driver.get('https://music.naver.com/listen/top100.nhn?domain='+str(list[m])+'V2&page='+str(k+1)+'')
        url = driver.current_url
        for i in tqdm(range(50)):
            if k == 0:
                lank = i+1
                #lank_text = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[2]/td[2]')
                song_name = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr['+ str(i+2) + ']/td[4]/a[4]/span').text
                artist_name = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr['+ str(i+2) + ']/td[5]/a').text
                img_url = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr['+ str(i+2) + ']/td[4]/a[1]/img').get_attribute('src')
                #print(lank, song_name, artist_name, img_url)
                name.loc[i, ["lank"]] = lank
                name.loc[i, ["song_name"]] = song_name
                name.loc[i, ["artist_name"]] = artist_name
                name.loc[i, ["img_url"]] = img_url
                #time.sleep(0.2)
            else:
                lank = i + 51
                # lank_text = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[2]/td[2]')
                song_name = driver.find_element_by_xpath(
                    '//*[@id="content"]/div[2]/div[1]/table/tbody/tr[' + str(i + 2) + ']/td[4]/a[4]/span').text
                artist_name = driver.find_element_by_xpath(
                    '//*[@id="content"]/div[2]/div[1]/table/tbody/tr[' + str(i + 2) + ']/td[5]/a').text
                img_url = driver.find_element_by_xpath(
                    '//*[@id="content"]/div[2]/div[1]/table/tbody/tr[' + str(i + 2) + ']/td[4]/a[1]/img').get_attribute(
                    'src')
                #print(lank, song_name, artist_name, img_url)
                name.loc[i + 50, ["lank"]] = lank
                name.loc[i + 50, ["song_name"]] = song_name
                name.loc[i + 50, ["artist_name"]] = artist_name
                name.loc[i + 50, ["img_url"]] = img_url
                #time.sleep(0.2)
    #print(name)
    return  name
for n in range(1):
    list = ['TOTAL_', 'DOMESTIC_', 'OVERSEA_']
    name = pd.DataFrame(columns=['lank', 'song_name', 'artist_name', 'img_url']).reset_index(drop=True)
    crwaling(n)
    writer = pd.ExcelWriter('./TOP100/FINAL.xlsx', engine='xlsxwriter')
    name.to_excel(writer, sheet_name= 'sheet{}'.format(n+1),encoding='utf8')
    # name.to_excel('./TOP100/{}.xlsx'.format(list[n]), encoding='utf8')
    writer.save()
driver.close()