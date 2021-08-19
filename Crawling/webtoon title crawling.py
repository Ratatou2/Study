import requests
from bs4 import BeautifulSoup as bs

URL = 'https://comic.naver.com/webtoon/weekday'
html = requests.get(URL)
soup = bs(html.text, 'html.parser')

titles = soup.find_all('a', {'class':'title'})

for title in titles:
    print(title.text)