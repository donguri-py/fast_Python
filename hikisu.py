def create_fullname(first, name):
    return first + " " + name

# fullname = create_fullname("山田", "太郎")
# print(fullname)

fullname = create_fullname("太郎", "山田")
print(fullname)


fullname = create_fullname(name="太郎", first="山田")
print(fullname)

fullname = create_fullname("山田", name="太郎")
print(fullname)

# キーワード引数が前に入ってはいけない！
# キーワード引数と位置引数が両方混在する場合には必ず位置引数が前にある必要がある！
fullname = create_fullname(first="山田", "太郎")

