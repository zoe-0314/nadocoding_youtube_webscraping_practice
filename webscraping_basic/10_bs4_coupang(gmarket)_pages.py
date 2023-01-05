import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}

for i in range(1,6):
    url = "https://browse.gmarket.co.kr/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=26&p={0}".format(i)

    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    #print(res.text)
    items = soup.find_all("div",attrs={"class":"box__item-container"})
    #print(items)
    #print(items[5].find("span",attrs={"class":"text__item"}).get_text())
    for item in items :
        name = item.find("span",attrs={"class":"text__item"}).get_text()
        price = item.find("strong",attrs={"class" : "text text__value"}).get_text()
        link = item.a["href"]
        #print("페이지: ", i, name, price)
        print(f"제품명 : {name}")
        print(f"가격 : {price}")
        print(f"링크 : {link}")
        print("-"*100) #줄긋기