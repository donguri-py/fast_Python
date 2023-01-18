# fruits = ["Apple", "Pineapple", "Orange"]
#
# try:
#     print(fruits[3])
#
# except IndexError as t:
#     print("インデックス範囲外", t)
#
# except Exception as t:
#     print(t)
#

ppap = ["Pen", "Pineapple", "Apple", "Pen"]

try:
    print(ppap[4])

except IndexError as e:
    print("範囲外" ,e)

except Exception as e:
    print(e)