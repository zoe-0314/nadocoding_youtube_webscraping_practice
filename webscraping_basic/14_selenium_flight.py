#네이버 항공권 사이트에서 제주국제공항 티켓 확인하기

import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

def wait_until(xpath_str): #값이 30초 이내에 로딩될 때까지 기다림
    WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,xpath_str)))

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/"
browser.get(url) #url로 이동

#time.sleep(2)
wait_until("//*[@id='__next']/div/div[1]/div[9]/div/div[2]/button[2]")
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div/div[2]/button[2]").click() #팝업 닫기

#가는 날 선택 클릭
#browser.find_element_by_link_text("가는 날").click() 
#begin_date = browser.find_element_by_xpath("//*[contains(text(),'가는 날')]").click()
begin_date = browser.find_element(By.XPATH,'//button[text()="가는 날"]').click()

#1초 대기
#time.sleep(1)
#값이 30초 이내에 로딩될 때까지 기다림
#WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//b[text() = "27"]')))
wait_until('//b[text() = "27"]')

#스크롤 조정
browser.execute_script("window.scrollTo(0, 300)")

#가는 날 일 선택
day27 = browser.find_elements(By.XPATH, '//b[text() = "30"]')
#print(len(day27))
day27[0].click()

#오는 날 일 선택
wait_until('//b[text() = "31"]')
day31 = browser.find_elements(By.XPATH,'//b[text() = "31"]')
day31[0].click()

#도착 버튼 클릭
wait_until('//b[text() = "도착"]')
arrival = browser.find_element(By.XPATH,'//b[text() = "도착"]')
arrival.click()
time.sleep(1)

#국내 선택
wait_until('//button[text() = "국내"]')
domestic = browser.find_element(By.XPATH,'//button[text() = "국내"]')
domestic.click()

#제주 선택
wait_until('//i[contains(text(),"제주국제공항")]')
jeju = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
jeju.click()

#검색 클릭
wait_until('//span[text()="항공권 검색"]')
search = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
search.click()

#값이 30초 이내에 로딩될 때까지 기다림
#첫번째 결과 출력
elem = WebDriverWait(browser,30).until(EC.presence_of_element_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

#브라우저 종료
#input('종료하려면 Enter 키를 입력하시오')
browser.quit()

