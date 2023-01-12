import re

g = "aaaaaaa《g》iiiiiiiiiiiiii《g》uuuuuuuuuuuuu《g》"

g = re.sub("《","",g)
print(g)

g = re.sub("[《》]","",g)
print(g)

g = re.sub("[^《》]","",g)
print(g)

a = "ジョバンニって誰なんだろう？"
a = re.sub("ジョバンニ","カンパネラ",a)
print(a)

gre = "ぺんりんごごごごごごごごごごごごごごパイナップルペン"

gre = re.sub("ご+","ご", gre)
print(gre)

w_cat = "吾輩は猫《である》"

w_cat = re.sub("[《》]","",w_cat)
print(w_cat)
