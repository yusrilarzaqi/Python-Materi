# Lathian

# Kalkulator sederhana
def main():
    print(20*"=")
    print("Kalkulator Sederhana")
    print(20*"=")

    num1 = float(input("> "))
    operator = input("Operator (+, -, x, /) : ")
    num2 = float(input("> "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '*' or operator == 'x':
        result = num1 * num2
    else:
        print('akhir program')

    print(f'Hasil : {result}')


if __name__ == "__main__":
    from os import system
    system('clear')
    main()
