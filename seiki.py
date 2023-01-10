import re

g_train = "ああああああああああああ《い》うううううううう《え》おおお"

# g_train = re.sub("《","", g_train)
# print(g_train)
#
# g_train = re.sub("[《》]", "",g_train)
# print(g_train)

g_train = re.sub("[^《》]", "", g_train)
print(g_train)