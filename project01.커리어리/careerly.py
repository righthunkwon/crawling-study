import requests
from bs4 import BeautifulSoup

# 개발자 커뮤니티 커리어리 검색어 크롤링
def crawl_careerly(keyword):
    url = f"https://careerly.co.kr/search?query=%{keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
        
    # item1
    title_containers = soup.select('h3.tw-font-bold.tw-text-color-text-bold.tw-line-clamp-1.tw-mb-1.search-result-card.tw-text-base')
    titles = [item.get_text(strip=True) for item in title_containers]

    # item2
    link_containers = soup.select('a.tw-bg-color-white')
    links = [f'https://careerly.co.kr{item["href"]}' for item in link_containers]
    
    # results
    results = [{'title': title, 'link': link} for title, link in zip(titles, links)]
    return results

keyword = input('터미널에 검색어 입력: ')
result = crawl_careerly(keyword)
print(result)