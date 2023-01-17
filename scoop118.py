# a = 123
#
# def shownum():
#     b = 456
#     print(a, b)
#
# shownum()

# a = 123
#
# def setnum():
#     b = 456
#
# setnum()
# print(a,b)

# a = 123
#
# def setlocal():
#     a = 456
#     print("local:",a)
#
# setlocal()
# print("global",a)

a = 123

def setglobal():
    global a
    a = 456
    print("local:",a)

setglobal()
print("global:",a)
