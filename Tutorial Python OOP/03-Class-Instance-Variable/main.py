class Hero():
    # Class Variable / Static Variable
    jumlah = 0

    def __init__(self, name):
        # attribute obj
        self.name = name
        Hero.jumlah += 1

# main program
shen=Hero('Shen')
print(Hero.jumlah)

vayne = Hero('Vayne')
print(Hero.jumlah)

