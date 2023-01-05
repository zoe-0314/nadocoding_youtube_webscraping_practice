import requests
import re
from bs4 import BeautifulSoup

url = "https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=26&p=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

#print(res.text)
items = soup.find_all("div",attrs={"class":"box__information"})
#rates = soup.select("span.image__awards-points>span.for-a11y")
#print(items)
#print(items[5].find("span",attrs={"class":"text__item"}).get_text())
for item in items :
    name = item.find("span",attrs={"class":"text__item"}).get_text()
    price = item.find("strong",attrs={"class" : "text text__value"}).get_text()
    rate = item.select("span.image__awards-points>span.for-a11y")
    rate_count = item.select("li.list-item__feedback-count>span.text")

    for i in rate:
        rate = i.get_text() #select는 리스트 형태라 하나씩 뽑아야 함
    if rate :
        rate = rate.replace('만족도 ','')
        rate = rate.replace('% 입니다.','')
    else :
        #rate = "평점 없음"
        print(" <평점 없는 상품은 제외합니다.>\n")
        continue

    for j in rate_count:
        rate_count = j.get_text() 
    if rate_count:    
        #rate_count = rate_count.replace('(','')
        #rate_count = rate_count.replace(')','')
        rate_count = rate_count[1:-1]
        rate_count = rate_count.replace(',','')
    else :
        rate_count = "평점 수 없음"
        print(" <평점 수가 없는 상품은 제외합니다.>\n")
        continue
    
    if "LG" in name :
        print(" <LG 전자 상품은 제외합니다.>\n")
        continue

    if float(rate) >= 90 and int(rate_count) >= 100: #리뷰평점 90% 이상, 리뷰 수 100개 이상
        print("이름 : ", name)
        print("가격 : ", price)
        print("평점 : ",rate)
        print("평점수 : ",rate_count)
        print("-"*100)
    

# for rate in rates:
#     if rate :
#         rate = rate.get_text()
#     else :
#         rate = "평점 없음"
#     print(rate)