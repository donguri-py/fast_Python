# class pico:
#     def setfruit(self):
#         self.apple = "りんご"
#         self.pine = "パイナップル"
#
# p1 = pico()
# p1.setfruit()
#
# print(p1.apple)
# print(p1.pine)

class pico:
    def setfruit(self, ap, pi):
        self.apple = ap
        self.pine = pi

pj = pico()
pj.setfruit("りんご", "パイナップル")

pe = pico()
pe.setfruit("Apple", "Pineapple")

print(pj.apple, pj.pine)
print(pe.apple, pe.pine)


class test:
    def teston(self, a, b):
        self.xyz = a
        self.abc = b

e = test()
e.teston("うんこ", "ブリブリ")

f = test()
f.teston("うほうほ", "ごりごり")

print(e.xyz, e.abc)
print(f.xyz, f.xyz)