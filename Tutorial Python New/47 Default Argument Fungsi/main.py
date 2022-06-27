"""DEFAULT ARGUMENT FUNGSI"""


def say_hello(nama="kamu") -> None:
    """fungsi dengan default argument"""
    print(f"Hallo {nama}")


say_hello()
say_hello("Yusril")


def sapa_dia(nama, pesan="apa kabar?") -> None:
    """fungsi dengan satu input biasa, dan satu default"""
    print(f"hai {nama}, {pesan}")


sapa_dia("Yusril")
sapa_dia("Bimo", "bagaimana kabarmu?")


def pangkat(angka=int, bilangan=2) -> int:
    return angka**bilangan


print(pangkat(2, 4))
print(pangkat(angka=10))


def fungsi(input1=1, input2=2, input3=3, input4=4) -> int:
    return input1 + input2 + input3 + input4


print(fungsi())
print(fungsi(input3=103))
