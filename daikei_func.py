# def daikei(ue,shita,hight):
#     return (ue + shita)*hight/2
#
# x = daikei(5,8,hight=4)
# print(x)
#
# def halfv(x):
#     return x / 2
#
# r = halfv(2)
# print(r)
#
# hhh = lambda x: x/2
#
# z = hhh(2)
# print(r)

def jug(x):
    return x % 3 == 0

num = [1,2,3,4,5,6]
fil = filter(jug,num)

print(list(fil))