def getPA(p, a):
    pa = "I have "+ str(p) + " pens. " + "I have " + str(a) + " apples."
    return pa

patext = getPA(3,4)
print(patext)

def subtract(a,b,c):
    d = a-b-c
    return d

result = subtract(b=3,c=4,a=12)
print(result)

def add(a, b=5):
    c = a+ b
    return c

result1 = add(3)
print(result1)

result2=add(3,6)
print(result2)