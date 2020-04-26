# 5.1 Создание веб-сервера
from yattag import Doc

doc, tag, text = Doc().tagtext()

with tag('html'):
    with tag('body'):
        with tag('table'):
            for x in range(1, 11):
                with tag("tr"):
                    for y in range(1, 11):
                        with tag("td"):
                            num = x * y
                            with doc.tag("a", href=f"http://{num}.ru"):
                                text(f"{num}")


result = doc.getvalue()
with open("1.5.3.html", "w") as f:
    f.write(result)
