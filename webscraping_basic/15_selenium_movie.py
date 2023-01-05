#BeautifulSoup으로 구글 무비 크롤링하기

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By 

#browser = webdriver.Chrome()
#browser.maximize_window() #창 최대화

url="https://play.google.com/store/movies?hl=ko"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

#browser.get(url)

# soup.select("div.wrap_thumb>a>img.thumb_img")
# movies = browser.find_elements(By.XPATH,'//span[text()="인기 차트"]//ancestor::section')
#movies_temp = soup.find_all("div",attrs={"class":"VfPpkd-EScbFb-JIbuQc"})
movies_temp = soup.find_all("div",attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})
#print(len(movies_temp))
for movie in movies_temp:
    #print(movie.get_text())
    title = movie.find("div",attrs={"class":"Epkrse"}).get_text()
    print(title)
#print(movies.text())
#print(movies_temp.get_text())

# with open("movie.html","w",encoding="utf8") as f:
#     #f.write(res.text)
#     f.write(soup.prettify()) #html문서를 예쁘게 출력