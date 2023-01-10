a = "           Pen Pineapple Apple Pen!   "
b = a.strip()
print(b)

a = "<<<<<<<<<<Pen <Pineapple Apple Pen!<<<<<<<<<<<<<<"
b = a.strip("<")
print(b)

a = "pineapple"
b = len(a)
print(b)

a = str(123)
print(a, type(a))

b = str(123.456)
print(b, type(b))

c = str(True)
print(c, type(c))

d = str([1,2,3])
print(d, type(d))


a = "PenPineappleApplePen"
b = a[3:12]
print(b)

ppap = "========I have a pen. I have a apple.==============="
b =ppap.strip("=")
print(b)
print(len(b))


