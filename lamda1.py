def add(a,b):
    c = a + b
    return c

print(add(3,4))

add_2 = add
print(add_2(3,4))


mlp = lambda a,b: a*b
print(mlp(3,4))


def make(a,b,c):
    d = a + " " + b + " " + c + " " + a + "!"
    return d
print(make("Pen", "Pineapple", "Apple"))

testlmda = lambda a,b,c,d,e: a+e+b+e+c+e+a+d
print(testlmda("Pen","Pineapple","Apple","!"," "))