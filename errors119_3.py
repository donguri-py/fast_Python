# a = "10"
# b = 5
# c = a-b
# print(c)

# input_file_name = input("ファイル名を入力")
# file_name = open(input_file_name)
# text = file_name.read()
# print(text)
# file_name.close()

# input_file_name = input("ファイルネームを")
# try:
#     file_name = open(input_file_name)
#     text = file_name.read()
#     print(text)
#     file_name.close()
# except:
#     print("該当ファイルがない")
#
# input_file_name = input("ファイル名")
#
# try:
#     with open(input_file_name) as f:
#         my_text = f.read()
#     print(my_text)
#
#     raise OSError
# except OSError:
#     print("ファイルの読み込みに失敗")

# a = "10"
# b = 5
#
# try:
#     c = a - b
#
# except NameError:
#     print("変数が設定されていないようです")
#
# except TypeError:
#     print("データ型が間違っているようです")
#
# except Exception:
#     print("例外発生です")

# a = "10"
# b = 5
#
# try:
#     c = a - b
#
# except NameError as ne:
#     print("変数が設定されていない")
#
# except TypeError as te:
#     print("データ型が間違っている")
#     print(te)
#
# except Exception as e:
#     print("例外発生")

# import requests
# input_url = input("URL")
#
# try:
#     r = requests.get(input_url, timeout=1)
#
# except requests.Timeout as err:
#     print("時間がかかる例外")
#     print(err)
#
# except Exception as e:
#     print("例外")

# import requests
# input_url = input("URL")
#
# try:
#     r = requests.get(input_url, timeout=1)
#
# except Exception as e:
#     print("例外")
# except requests.Timeout as err:
#     print("時間がかかるエラー")
#     print(err)


# x = "Hello Java"
#
# try:
#     file_name = open("text.text")
#     x = file_name.read()
#     file_name.close()
# except Exception as e:
#     pass
#
# print(x)

#
# text = ""
# input_file_name = input("ファイル名")
#
# try:
#     file_name = open(input_file_name)
#     text = file_name.read()
#     file_name.close()
#
# except Exception as e:
#     print("該当ファイルなし")
#
# else:
#     print("ありがとう！")
#
# print(text)

a = "10"
b = 5
c = 0

try:
    c = a-b

except NameError as ne:
    print("変数未設定")

except TypeError as te:
    print("データ型間違い")

except Exception as e:
    print("例外")

else:
    print("例外")

finally:
    print("tryの終了")