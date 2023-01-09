a = {"ペン", "りんご", "パイナップル"}
print(a)

a.add("いちご")
print(a)

a.add("ペン")
print(a)

b = "りんご" in a
print(b)

a = ["ペン", "りんご", "パイナップル", "ペン"]
b = set(a)
print(b)

ppap = ["Pen", "Pineapple", "Apple", "Pen", "Apple", "Pico", "Pen"]
x = set(ppap)
print(x)