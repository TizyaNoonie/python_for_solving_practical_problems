# 1.3 Знакомство с BeautifulSoup
import requests as rq
from bs4 import BeautifulSoup

url = r"https://stepik.org/media/attachments/lesson/245130/6.html"

page = rq.get(url)
soup = BeautifulSoup(page.content, "html.parser")

table = soup.find('table', attrs={'class': 'wikitable sortable'})
cnt = 0
for tr in soup.find_all('tr'):
    cnt += 1
    for td in tr.find_all(['td', 'th']):
        cnt *= 2
print(cnt)  # 94596065609609271052308
