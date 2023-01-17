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

class Pico3:
    def setFruit(self, ap, pi):
        self.apple = ap
        self.pine = pi

pj = Pico3()
pj.setFruit("りんご", "パイナップル")

pe = Pico3()
pe.setFruit("Apple", "Pineapple")

print(pj.apple, pj.pine)
print(pe.apple, pe.pine)