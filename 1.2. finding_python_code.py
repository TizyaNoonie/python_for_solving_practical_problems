# 1.2 Обработка html как текста
import re
import requests as rq

from collections import Counter

url = r"https://stepik.org/media/attachments/lesson/209719/2.html"


def count_code_samples(url):
    d = {}
    req = rq.get(url)
    source_code = req.text
    pattern = r'<code>(.*?)</code>'
    results = re.findall(pattern, source_code)
    for item in results:
        if item not in d:
            d[item] = 0
        d[item] += 1

    return Counter.most_common(d)


print(count_code_samples(url))  # else except finally
