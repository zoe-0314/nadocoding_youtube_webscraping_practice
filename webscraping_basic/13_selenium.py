#크롬 드라이버 설치
# pip install selenium
# pip install selenium==3.141.0
from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
#browser = webdriver.Chrome("C:/Users/이태완/Desktop/coding study/chromedriver.exe")
# browser = webdriver.Chrome()
# browser.get("http://naver.com")

#로그인
#elem = browser.find_element_by_class_name("link_login")
#elem.click()

#뒤로가기
#browser.back()

#앞으로 가기
#browser.forward()

#새로고침
#browser.refresh()

#검색창에 글자 입력
# elem = browser.find_element_by_id("query")

# from selenium.webdriver.common.keys import Keys #키보드의 키를 컴퓨터에 전달하기 위해 사용

# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)

# a태그 가져오기
#elem = browser.find_element_by_tag_name("a")
#print(elem)

# elem = browser.find_elements_by_tag_name("a")
# print(elem)
# for e in elem:
#     e.get_attribute("href")
#     print(e)


#----daum
# browser.get("http://daum.net")
# elem = browser.find_element_by_name("q")
# print(elem)
# elem.send_keys("나도코딩")
# #from selenium.webdriver.common.keys import Keys
# #elem.send_keys(Keys.ENTER)
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[3]")
# print(elem)
# elem.click()


# #브라우저 종료
# browser.quit() #브라우저 전체 종료

import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id,pw 입력
browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()
time.sleep(3)

# 5. id 를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
#browser.close() #현재 탭만 종료
browser.quit() #전체 브라우저 종료