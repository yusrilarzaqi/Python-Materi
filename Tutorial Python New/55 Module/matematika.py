# Module matematika


def tambah(*args: float):
    result = 0
    for num in args:
        result += num
    return result


def kali(*args):
    result = 1
    for num in args:
        result *= num
    return result


def pangkat(n: int):
    return lambda num: num**n
