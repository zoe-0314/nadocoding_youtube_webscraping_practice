#daum 최근 5년 역대 관객 순위 1 - 5위 영화 이미지 다운받기

import requests
from bs4 import BeautifulSoup

for i in range(1,6):
    year = 2022 - i
    url="https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    print(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")

    #images = soup.find_all("div",attrs={"class":"wrap_thumb"})
    images = soup.select("div.wrap_thumb>a>img.thumb_img")
    # for image in images:
    #     print(images)
    for idx, image in enumerate(images):
        #print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//") :
            image_url = "https:" + image_url
        if 'Fmovie' not in image_url:
            continue
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year,idx+1),"wb") as f:
            f.write(image_res.content)
        
        if idx >=4: # 상위 5개의 이미지만 다운로드
            break