# 5.1 Создание веб-сервера
# Sometimes I start to think that I might be really clever
from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        with tag('table'):
            for x in range(1, 11):
                with tag("tr"):
                    for y in range(1, 11):
                        with tag("td"):
                            text(f"{x * y}")


result = doc.getvalue()
with open("1.5.2.html", "w") as f:
    f.write(result)
