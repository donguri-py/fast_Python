# a = 123
#
# def shownum():
#     b = 456
#     print(a, b)
#
#
# shownum()
#
# a = 123
#
# def setnum():
#     b = 456
#
# setnum()
# print(a, b)

#
# a = 123
#
# def setlocal():
#     a = 456
#     print("Local:", a)
#
# setlocal()
#
# print("Global:", a)


a = 123

def setglobal():
    global a
    a = 456
    print("Local:", a)

setglobal()

print("Global:" , a)