# 3.2 OpenStreetMap как пример XML
import json
import xmltodict

with open("map2.osm", "r", encoding="utf8") as f:
    content = f.read()

parsed_xml = xmltodict.parse(content)
output_dict = json.loads(json.dumps(parsed_xml))
output_dict = output_dict["osm"]

with_tag = 0
without_tag = 0
for node in output_dict["node"]:
    if "tag" in node:
        with_tag += 1
    else:
        without_tag += 1

print(with_tag, without_tag)  # 316 6166
