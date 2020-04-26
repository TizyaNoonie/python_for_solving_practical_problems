# When you are tired of writing a downloading script for every task
import requests as rq

# write a name for your file you need to download
filename = "map4.osm"

# write url of the file
url = "https://stepik.org/media/attachments/lesson/245681/map2.osm"

# run the script
page = rq.get(url)
with open(filename, "wb") as f:
    f.write(page.content)
