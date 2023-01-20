# class Item:
#     pass
#
# x = Item()
# x.name = 'book'
# print(x.name)

import requests

request = requests.get("https://sai-lab.co.jp/")

print(request.text)