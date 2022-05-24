def main(sisi):
    for i in range(sisi, 0, -1):
        for _ in range(i):
            print(' ', end="")
        for _ in range(0, i):
            print(f'+', end="")
        print()


main(10)
