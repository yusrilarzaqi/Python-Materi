class Hero():
    # Class Variable
    jumlah_hero = 0
    def __init__(self, name, health):
        # instance variable
        self.name = name
        self.health = health
        Hero.jumlah_hero += 1

    # Void Function, Method tanpa return
    def who(self):
        print(f'Name : {self.name}')

    # Method dengan argument
    def healthUp(self, up):
        self.health += up

    # Method dengan return
    def getHealth(self):
        return self.health

# main program
shen = Hero('Shen', 650)
shen.who()
print(shen.jumlah_hero)
print(shen.getHealth())
shen.healthUp(40)
print(shen.getHealth())

