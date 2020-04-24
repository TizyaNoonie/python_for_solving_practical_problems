# 1.4 Использование BeautifulSoup
# code works in the same way as in the previous task
import requests as rq
from bs4 import BeautifulSoup

url = r"https://stepik.org/media/attachments/lesson/209723/4.html"

page = rq.get(url)
soup = BeautifulSoup(page.content, "html.parser")

total_sum = 0
for element in soup.find_all("td"):
    total_sum += int(element.text)

print(total_sum)  # 29536
