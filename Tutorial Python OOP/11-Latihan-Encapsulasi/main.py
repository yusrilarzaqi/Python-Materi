class Hero:
    # private var
    __jumlah = 0

    def __init__(self, n, h, at, ar):
        self.__name = n
        # base stat
        self.__health_base = h
        self.__attackDamage_base = at
        self.__arrmor_base = ar
        self.__level = 1
        self.__exp = 0

        # max stat

        self.__health_max = self.__health_base * self.__level
        self.__attackDamage = self.__attackDamage_base * self.__level
        self.__arrmor = self.__arrmor_base * self.__level

        self.__health = self.__health_max
        Hero.__jumlah += 1

    @property
    def show(self):
        return f"{self.__name} : \n\tLevel : {self.__level} \n\tHealth : {self.__health}/{self.__health_max} \n\tAttack Power : {self.__attackDamage}\n\tArrmor : {self.__arrmor}"

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, up):
        self.__exp += up
        if self.__exp >= 100:
            self.__level += 1
            self.__exp = 100

            self.__health_max = self.__health_base * self.__level
            self.__attackDamage = self.__attackDamage_base * self.__level
            self.__arrmor = self.__arrmor_base * self.__level

    def serang(self, enemy):
        self.gainExp = 50

        enemy.__health -= self.__attackDamage - (enemy.__arrmor * 0.1)


# main program
def main():

    Shen = Hero("Shen", 640, 55, 42)
    print(Shen.show, "\n")

    Vayne = Hero("Vayne", 560, 64, 38)
    print(Vayne.show)

    print("Pertempuran ".center(15, "-"))
    Shen.serang(Vayne)
    Shen.serang(Vayne)
    Shen.serang(Vayne)

    print("Akhir".center(15, "-"))
    print(Shen.show)
    print(Vayne.show)


if __name__ == "__main__":
    main()
