import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status() # 200 OK 코드가 아닌 경우 에러 발동

soup = BeautifulSoup(res.text,"lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all("a",attrs={"class":"title"})
# a element의 class 속성이 title인 모든 element를 반환
#for cartoon in cartoons:
#    print(cartoon.get_text())

webtoons=[]
for cartoon in cartoons:
    webtoons.append(cartoon.get_text())


for webtoon in webtoons:
    print("\n", webtoon)
