a = "私はペンとりんごを持っています。"
b = a.find("りんご")
print(b)


a = "私はペンとりんごを持っています。"
b = a.find("パイナップル")
print(b)


b = "りんご" in a
print(b)

c = "パイナップル" in a
print(c)

a = "私はペンとリンゴを持っています。私はペンとパイナップルを持っています。"
b = a.count("ペン")
print(b)

wagahai = "吾輩は猫である。吾輩は犬である。吾輩は鳥である。"
b = wagahai.find("吾輩")

print(b)