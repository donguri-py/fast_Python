pen = "Pen"
apple = "Ringo"

def setppap():
    global apple
    global pen
    apple = "Apple"
    pine = "Pineapple"
    ppap = pen + " " + pine + " " + apple + " " + pen + "!"
    return ppap
x = setppap()

print(x)