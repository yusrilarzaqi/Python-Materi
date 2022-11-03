# __main__ adalah top level code environment.

# __name__ == "__main__"
## ini akan terjadi jika berada program utama

## Nilai pada file program utama
print(f"nilai __name__ pada main.py = '{__name__}'")

## __name__ pada file program external
import fungsi

## Contoh penggunaan

# Deklarasi
def add(num1: int, num2: int) -> int:
    return num1 + num2


# fungsi utama
if __name__ == "__main__":
    print(f"hasil = {add(10, 20)}")

import package
