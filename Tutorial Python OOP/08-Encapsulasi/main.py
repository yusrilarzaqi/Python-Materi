class Hero:
    def __init__(self, name: str, health: int, attackDamage: int) -> None:
        self.__name = name
        self.__health = health
        self.__attackDamage = attackDamage

    # Getter
    @property
    def getName(self):
        return self.__name

    # Setter
    def setName(self, name: str) -> None:
        """Program Set Nama Hero"""
        self.name = name

    # Attack
    def attack(self, enemy):
        self.__health -= enemy.__attackDamage
        return self.__health


# main program
Shen = Hero("Shen", 640, 67)
Vayne = Hero("Vayne", 560, 77)

s = Shen.attack(Vayne)
print(s)


# ganti nama
Shen.setName("Shen Baru")
print(Shen.getName)
