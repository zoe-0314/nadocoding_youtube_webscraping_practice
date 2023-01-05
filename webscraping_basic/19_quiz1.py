# Quiz) 부동산 매물(송파 헬리오시티) 정보를 스크래핑 하는 프로그램을 만드시오
#[조회 조건]
# 1. http://daum.net 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보

#[출력 결과]
#========== 매물 1 ==========
# 거래 : 매매
# 면적 : 84/59 (공급/전용)
# 가격 : 165,000 (만원)
# 동 : 214동
# 층 : 고/23
#========== 매물 2 ==========
# ...

#[주의 사항]
#- 실습하는 시점에 위 매물이 없다면 다른 곳으로 대체 가능

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


browser = webdriver.Chrome()
browser.maximize_window()

def hand_scroll(y):
    try:
        right_info=browser.find_element(By.XPATH,'//*[@data-testid="ScrollView"]')
        browser.execute_script("arguments[0].scrollBy(0,200)",right_info)

    except:  # 끝 도달시
        return False

url = "https://realty.daum.net/home/apt/map"
browser.get(url)

#아파트 검색
browser.find_element(By.XPATH,'//*[@class="input-wrap"]//input').send_keys("한양수자인에듀힐즈")
time.sleep(2)
browser.find_element(By.XPATH,'//button[@class="btn-search"]').click()

#스크롤바 내리기
time.sleep(2)
right_info=browser.find_element(By.XPATH,'//*[@data-testid="ScrollView"]')
browser.execute_script("arguments[0].scrollBy(0,500)",right_info)

#prev_height = browser.execute_script("arguments[0].scrollBy(0,0)",right_info)
#time.sleep(2)
#right_info=browser.find_element(By.XPATH,'//*[@data-testid="ScrollView"]')


#더보기 버튼
more_view_btn = browser.find_element(By.XPATH,'//*[@id="__next"]/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[4]/div/div[1]/div[2]/div/div[3]/div/div[2]/div[3]/div/div[1]/div[1]')

#더보기 버튼이 존재하면, 클릭 후 스크롤 내리기
try:
    while True:
        if more_view_btn:
            more_view_btn.click()
            time.sleep(1)
            hand_scroll(200)
except:
    pass

#스크롤을 내려 획득한 실거래가 부분만 가져오기
soup = BeautifulSoup(browser.page_source,"lxml")
#print(soup)
house_info = soup.find_all("div",attrs={"class":"css-1dbjc4n r-1awozwy r-p9m3gb r-17leim2 r-1sxrcry r-13awgt0 r-1mlwlqe r-18u37iz r-17j37da r-lgpkq r-qi0n3 r-c9eks5 r-k5i03q"})
#house_info_count = len(house_info)

#매물 순서 변수 설정
house_info_count=1

#각 매물별 정보 보이기
for house in house_info:
    #house.find_all("div",{"class":"css-1563yu1"})[0] #계약일
    buy_type=house.find_all("div",{"class":"css-1563yu1"})[1].get_text() #매매
    price=house.find_all("div",{"class":"css-1563yu1"})[2].get_text() #가격
    house_type=house.find_all("div",{"class":"css-1563yu1"})[3].get_text() #타입(면적)
    floor=house.find_all("div",{"class":"css-1563yu1"})[4].get_text() #층

    print(f"========== 매물 {house_info_count} ==========")
    print("거래 : ",buy_type)
    print("타입(면적) : ",house_type)
    print("가격 : ",price)
    print("층 : ",floor,"층")

    house_info_count+=1



