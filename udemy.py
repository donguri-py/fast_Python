a = [1,2,3,4,5,6,7]
b = []

for c in a:
    b.append(c * 2)

print(b)

b = [c*2 for c in a]
print(b)

b = [c*2 for c in a if c < 5]
print(b)