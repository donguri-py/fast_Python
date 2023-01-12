def job(pos, *args):
    print(pos, args)

job(1, 2, 3)


def job(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwargs[kwarg])

args = [1, 2]
kwargs = {'three': 3, 'four': 4}

job(*args, **kwargs)


num = [1, 2, 3, 4]

even = filter(lambda x: x % 2 == 0, num)

print(list(even))