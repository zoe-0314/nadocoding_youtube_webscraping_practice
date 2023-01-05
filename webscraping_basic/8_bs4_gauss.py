import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=799793&page=5"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#print(soup)
#cartoons = soup.find_all("td",attrs={"class":"title"})

# print(cartoons[0].a.get_text())
# print("http://comic.naver.com"+cartoons[0].a["href"])

# 만화 제목 + 링크 가져오기
# for cartoon in cartoons:
#     title=cartoon.a.get_text()
#     link="http://comic.naver.com"+cartoon.a["href"]
#     print(title, link)


# 평점 구하기
total_rates = 0
cartoons = soup.find_all("div",attrs={"class":"rating_type"})
print(type(cartoons))
for cartoon in cartoons :
    rate=cartoon.find("strong").get_text()
    print(rate)
    total_rates +=float(rate)
print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates/len(cartoons))