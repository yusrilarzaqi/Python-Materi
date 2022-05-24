class Hero():
    # Class akan mengeksekusi pertama
    def __init__(self, name, health, attack, arrmor):
        self.name = name
        self.health = health
        self.attack = attack
        self.arrmor = arrmor

    def show_info(self):
        print(f'Name : {self.name}\nHealth : {self.health}\nAttack : {self.attack}\nArrmor : {self.arrmor}')

# Main program
shen = Hero('Shen', 630, 56, 60)
shen.show_info()
