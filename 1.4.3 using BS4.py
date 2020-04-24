# 1.4 Использование BeautifulSoup
# Requires installation of 'html5lib'. No additional import is needed
# For this task you can use code from the previous ones though. Just need to change the url value.

import requests as rq
from bs4 import BeautifulSoup

url = r"https://stepik.org/media/attachments/lesson/209723/5.html"

page = rq.get(url)
soup = BeautifulSoup(page.content, "html5lib")

total_sum = 0

for element in soup.find_all("td"):
    total_sum += int(element.text)

print(total_sum)  # 28734
