def getNumber():
    a = 123
    return a

b = getNumber()
print(b)

def add(a,b):
    c = a + b
    return c

result1 = add(3,4)
print(result1)

result2 = add(7,8)
print(result2)

def addmlp(a,b):
    c = a+b
    d = a*b
    return (c,d)
result1 = addmlp(3,4)
print(result1)