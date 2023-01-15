# def test(num):
#     return num + 10
#
# map_list = [10,20,30]
# map_list2 = map(test,map_list)
#
# print(map_list)
#
# for x in map_list2:
#     print(x)

# def check_10n(num):
#     return num % 10 == 0
#
# check_list = [10,20,22,25,30,40,50]
# checked_list = list(filter(check_10n, check_list)
#
# print(checked_list)

def my_func(x):
    return x > 5

my_list = list(filter(my_func, [7,4,2,10]))
print(my_list)