#구글 무비에서 할인하는 영화 정보만 스크래핑하기


# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.by import By 

# #browser = webdriver.Chrome()
# #browser.maximize_window() #창 최대화

# url="https://play.google.com/store/movies?hl=ko"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko"}
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,"lxml")

# #browser.get(url)


# #movies_temp = soup.find_all("div",attrs={"class":"VfPpkd-EScbFb-JIbuQc"})
# movies_temp = soup.find_all("div",attrs={"class":"VfPpkd-EScbFb-JIbuQc UVEnyf"})
# #print(len(movies_temp))
# for movie in movies_temp:
#     #print(movie.get_text())
#     title = movie.find("div",attrs={"class":"Epkrse"}).get_text()
#     print(title)
# #print(movies.text())
# #print(movies_temp.get_text())

# # with open("movie.html","w",encoding="utf8") as f:
# #     #f.write(res.text)
# #     f.write(soup.prettify()) #html문서를 예쁘게 출력

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Chrome()
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
