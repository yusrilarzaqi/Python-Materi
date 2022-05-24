class Hero:
    def __init__(self, name, health, attack):
        self.__name = name
        self.__health = health
        self.__attack = attack

    @property
    def getInfo(self):
        pass

    @getInfo.getter
    def getInfo(self):
        return f"Name : {self.__name}\n\tHealth : {self.__health}\n\tAttack : {self.__attack} "

    def attack(self, enemy):
        # Self lawan enemy
        # health enemy berkurang
        # self tambah att & healthi
        enemy.__health -= self.__attack - (enemy.__health * .01)
        self.__attack += (self.__attack * .2)
        self.__health += (self.__health * .2)



vayne = Hero('Vayne', 550, 56)
shen = Hero("Shen", 640, 44)
print(shen.getInfo)
print(vayne.getInfo)

shen.attack(vayne)


print(shen.getInfo)
print(vayne.getInfo)

