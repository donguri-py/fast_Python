def fizzbuzz(x):
    if x % 15 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)

a = fizzbuzz(3)
b = fizzbuzz(5)
c = fizzbuzz(30)
d = fizzbuzz(49)

# def fizzbuzz(x):
#     if x % 15 == 0:
#         result = "FizzBuzz"
#     elif x % 3 == 0:
#         result = "Fizz"
#     elif x % 5 == 0:
#         result = "Buzz"
#     else:
#         result = x
#     return result
#
# r1 = fizzbuzz(3)
# r2 = fizzbuzz(5)
# r3 = fizzbuzz(30)
# r4 = fizzbuzz(49)
# print(r1,r2,r3,r4)