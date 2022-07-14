""" BAISC """


def tambah(*args):
    return sum(args)


def kali(*args):
    result = 1
    for num in args:
        result *= num
    return result
