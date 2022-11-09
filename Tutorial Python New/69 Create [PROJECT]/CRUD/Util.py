from random import choice
from string import ascii_letters

def random_string(length: int) -> str:
    return ''.join(choice(ascii_letters) for i in range(length))
