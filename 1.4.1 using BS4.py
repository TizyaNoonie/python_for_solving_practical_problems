# 1.4 Использование BeautifulSoup
import requests as rq
from bs4 import BeautifulSoup

url = r"https://stepik.org/media/attachments/lesson/209723/3.html"

req = rq.get(url)
soup = BeautifulSoup(req.content, "html.parser")

total_sum = 0

results = soup.find_all("td")
for result in results:
    total_sum += int(result.text)

print(total_sum)  # 1005425
