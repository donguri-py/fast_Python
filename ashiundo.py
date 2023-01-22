def job(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwargs[kwarg])

args = [1, 2]
kwargs = {'three': 3, 'four': 4}

job(*args, **kwargs)