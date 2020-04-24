# 1.1 Скачивание web-страниц
import requests as rq

url = r"https://stepik.org/media/attachments/lesson/209717/1.html"


def most_freqent(url):
    req = rq.get(url)
    source_code = req.text
    python_count = source_code.count("Python")
    c_plusplus_count = source_code.count("C++")
    print(python_count, c_plusplus_count)
    if python_count > c_plusplus_count:
        return "Python"
    else:
        return "C++"


print(most_freqent(url))
