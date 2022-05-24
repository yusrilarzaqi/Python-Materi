class Team:
    def setTeam(self, team):
        self.__team = team

    def showTeam(self):
        print(self.__team)

class Type_hero:
    def setType(self, typ):
        self.__typ = typ

    def show_type(self):
       print(self.__typ)

class Hero(Team, Type_hero):
    def __init__(self, name):
        self.__name = name

    def show_name(self):
        print(self.__name)

shen=Hero('Shen')
shen.setTeam('Red')
shen.setType('Tank')

shen.showTeam()
shen.show_type()
shen.show_name()
