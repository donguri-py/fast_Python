# def intro(name: str, age: int):
#     print(f"名前: {name}, 年齢: {age}")
#
# intro("田中次郎",20)


# def func(name: str = "noname", age: int=0):
#     print(f"name: {name}, age:{age}")
#
# func("mike")
# func(age=80)
# func()


# def func(datas: list = []):
#     datas.append(1)
#     print(datas)
#
# func()
# func()

# def func(datas: list = None):
#     if datas is None:
#         datas = []
#     datas.append(1)
#     print(datas)
# func()
# func()

# def func(arg, /):
#     print(arg)
#
# func(0)
# func(arg=0)

def add(num1, num2, /, num3):
    return num1 + num2 + num3
x = add(1,2,num3=3)
print(x)

add(num1=1, 2, num3=3)












