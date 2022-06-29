""" Type Hints untuk Fungsi """

# Bentuk starndar fungsi yang kita ketahui


"""
def fungsi(parameter):
    # statment
    print(parameter)


fungsi(1)
fungsi("Yusril Arzaqi")
fungsi(True)
"""


def kuadrat(argument: int) -> int:
    """FUNGSI DENGAN HINTS"""
    return argument**2


print(kuadrat(10))


def display(argument: str) -> None:
    print(argument)
