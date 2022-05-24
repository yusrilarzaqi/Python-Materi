class Hero:
    def __init__(self, n, h):
        self.__name = n
        self.__health = h

    def showInfo(self):
        print("Info Hero")
        print(f'{self.__name} \nHealth : {self.__health}')

class Hero_tank(Hero):
    def __init__(self, name):
        super().__init__(name, 670)

    # override
    def showInfo(self):
        print("Show Info Hero Tank")
        print(f'{self.__name}\nHealth : {self.__health} ')

class Hero_support(Hero):
    def __init__(self, name):
        super().__init__(name, 659)

    def showInfo(self):
        print("Show Info Support")
        print(f'{self.__name}\nHealth : {self.__health} ')


Shen = Hero("Shen", 660)
Shen.showInfo()

# Maokai = Hero_tank("Maokai")
# Maokai.showInfo()

# Leona = Hero_support('Leona')
# Leona.showInfo()




