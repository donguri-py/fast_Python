def makePPAP(a,b,c):
    p = a + b + c + a
    return p

ppap = makePPAP("Pen", "Pineapple","Apple")
print(ppap)


def showppap(*a):
    print(a)

    ppap = " ".join(a)
    ppap += "!"

    print(ppap)

showppap("Pen","Pineapple","Apple","Pen","TSUIKA")


def showdic(**a):
    print(a)

showdic(pen=3, pine=4, apple=5,tomato=99)
