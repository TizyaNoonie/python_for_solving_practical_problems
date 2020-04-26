# 3.4 Как добыть нужную информацию, не читая документацию к API
import xmltodict
import json

with open("map4.osm", "r", encoding="utf-8") as f:
    content = f.read()
    xml_dict = xmltodict.parse(content)

normal_dict = json.loads(json.dumps(xml_dict))["osm"]


def count_fuels(sub_dictionary):
    counter = 0
    for item in sub_dictionary:
        if "tag" in item:
            tag = item.get("tag")
            if isinstance(tag, dict):
                if tag.get("@v") == "fuel":
                    counter += 1
            elif isinstance(tag, list):
                for sub_d in tag:
                    if sub_d.get("@v") == "fuel":
                        counter += 1
    return counter


print(count_fuels(normal_dict["node"]) + count_fuels(normal_dict["way"]))  # 27
