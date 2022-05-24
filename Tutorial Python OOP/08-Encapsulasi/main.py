class Hero:
    def __init__(self, name, health, attackDamage):
        self.__name = name 
        self.__health = health
        self.__attackDamage = attackDamage

    # Getter
    def getName(self):
        return self.__name

    # Setter
    def setName(self):
        return self.__name

    # Attack
    def attack(self, enemy):
        self.__health -= enemy.__attackDamage
        return self.__health

# main program
Shen = Hero('Shen', 640, 67)
Vayne = Hero('Vayne', 560, 77)

s =Shen.attack(Vayne)
print(s)
