# 3.3 Обработка XML с разным количеством вложенных тэгов
import json
import xmltodict

with open("map3.osm", "r", encoding="utf-8") as f:
    content = f.read()

xml_dict = xmltodict.parse(content)
dic = json.loads(json.dumps(xml_dict))["osm"]

counter = 0

for node in dic.get("node"):
    if "tag" in node:
        tag = node["tag"]
        if isinstance(tag, dict):
            if tag["@v"] == "fuel":
                counter += 1
        elif isinstance(tag, list):
            for item in tag:
                if item.get("@v") == "fuel":
                    counter += 1

print(counter)  # 15
