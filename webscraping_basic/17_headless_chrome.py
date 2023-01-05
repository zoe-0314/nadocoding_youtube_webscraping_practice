#headless를 이용하여 크롬 브라우저를 켜지 않고 스크래핑하기

import requests
from bs4 import BeautifulSoup
from selenium import webdriver


option = webdriver.ChromeOptions()
option.headless = True
option.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=option)
browser.maximize_window()

#페이지 이동
url="https://play.google.com/store/movies?hl=ko"
browser.get(url)

#스크롤 내리기
#모니터(해상도) 높이인 1080 위치로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,1080)") 
# browser.execute_script("window.scrollTo(0,2080)") 

#화면 가장 아래로 스크롤 내리기
#browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

import time
interval = 2 # 2초에 한번씩 스크롤 내림

#현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복 수행
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    #페이지 로딩 대기
    time.sleep(interval)

    #현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png") #스크린샷 저장하기


soup = BeautifulSoup(browser.page_source,"lxml")
movies = soup.find_all("div",attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})
for movie in movies:
    #print(movie.get_text())
    title = movie.find("div",attrs={"class":"Epkrse"}).get_text()
    #print(title)

    #할인 전 가격
    original_price = movie.find("span",attrs={"class":"SUZt4c P8AFK"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title,"   < 할인되지 않은 가격")
        continue
    
    #할인된 가격
    price = movie.find("span",attrs={"class":"VfPpfd VixbEe"}).get_text()

    #링크 정보
    link = movie.find("a",attrs={"class":"Si6A0c ZD8Cqc"})["href"]
    # 올바른 링크 https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ","https://play.google.com"+link)
    print("-"*120)

    browser.quit()