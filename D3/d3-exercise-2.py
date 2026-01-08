from math import *
from statistics import *
import json as js

item = {
    "name": "Book of the knowledge",
    "rarity": "common",
    "durability": 100,
}

item["bookmark-page"] = 55

js_str = js.dumps(item, indent=2)
print("JSON string", js_str)

with open("d3-test-json.json", "w") as f:
    f.write(js_str)


with open("d3-test-json.json", "r") as f:
    loaded_item = js.load(f)

print(loaded_item)
print(f"Name: {loaded_item['name']}")
print(f"Bookmark-page: {loaded_item["bookmark-page"]}")



