# def add(num1, *,num2, num3):
#     return num1 + num2 + num3
#
# x = add(1, num2=2, num3=3)
# print(x)
#
# y = add(1,2,3)
# print(y)


def add(num1, /,num2, num3):
    return num1 + num2 + num3

x = add(1,2,3)
print(x)