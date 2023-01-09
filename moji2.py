a = "ペンPicoパイナップルPicoりんごPicoペン"
b = a.split("Pico")
print(b)

a = ["ペン", "パイナップル","りんご","ペン"]
b = "Pico".join(a)
print(b)


a = "ペンPicoパイナップルPicoりんごPicoペン"
b = a.replace("Pico", "=")
print(b)

ppap = "PenPineappleApplePen"
b = ppap.replace("Pen", "LongPen")
print(b)