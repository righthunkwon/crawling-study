import requests
from bs4 import BeautifulSoup
import time
import random

# 네이버 뉴스 제목 및 링크 데이터 크롤링
def crawl_news(keyword, lastpage):
    results = []
    for i in range(1, int(lastpage) * 10, 10):
        url = f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}&start={i}'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        items = soup.select('.news_tit')

        for item in items:
            title = item.text
            link = item.attrs['href']
            results.append({'title': title, 'link': link})
        
        random_wait_time = random.uniform(2, 4)
        time.sleep(random_wait_time)

    return results

keyword = input('터미널에 검색어 입력: ')
lastpage = input('마지막 페이지번호 입력: ')

results = crawl_news(keyword, lastpage)
print(results)
print('total results: ', len(results))
