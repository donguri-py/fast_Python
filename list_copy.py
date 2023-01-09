a = [1,2,3]
b = a
b[1] = 10

print(a)
print(b)

a = [1,2,3]
b = a.copy()
b[1] = 10

print(a)
print(b)