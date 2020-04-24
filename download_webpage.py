import requests as rq

url = r"https://ru.wikipedia.org/wiki/Python"

req = rq.get(url)
web_page = req.text
print(web_page)