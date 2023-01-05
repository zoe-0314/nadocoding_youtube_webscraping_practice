from selenium import webdriver


option = webdriver.ChromeOptions()
option.headless = True
option.add_argument("window-size=1920x1080")
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36") 
#headlesschrome일 경우 useragent값이 날아갈 수 있음 그래서 이렇게 별도로 설정해주어야 함

browser = webdriver.Chrome(options=option)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()
