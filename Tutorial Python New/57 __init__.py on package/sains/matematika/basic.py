def tambah(*args):
    return sum(args)


def kali(*args: int):
    result = 1
    for num in args:
        result *= num
    return result
