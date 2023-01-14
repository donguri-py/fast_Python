def show(a,b,callb):
    c = callb(a,b)
    print(c)

def add(a,b):
    return a+b

show(3,4,add)

