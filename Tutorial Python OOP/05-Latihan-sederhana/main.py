class Hero():
    jumlah =0

    def __init__(self, name, health, att, arrmor):
        self.name = name
        self.health = health
        self.att = att
        self.arrmor = arrmor

        Hero.jumlah += 1

    def serang(self, enemy):
        print(f'{self.name} menyerang {enemy.name}')
        enemy.diserang(self, self.att)

    def diserang(self, enemy, attackLawan):
        print(f'{self.name} diserang {enemy.name}')
        attackDiterima = attackLawan - (self.arrmor * 0.2)
        print(f'Damage yang dihasilkan : {attackDiterima}')
        self.health -= attackDiterima
        print(f'Health tersisa : {self.health}')

    @property
    def getInfo(self):
        pass
      
    @getInfo.getter
    def getInfo(self):
      return f'Name : {self.name}\n\tHealth : {self.health}\n\tAttack Power : {self.att}\n\tArrmor : {self.arrmor}'
    
#Main program
Shen = Hero('Shen', 640, 64, 43)
Vayne = Hero('Vayne', 580, 72, 39)
print(Shen.getInfo)
print(Vayne.getInfo)
print()
Shen.serang(Vayne)
print()
print(Vayne.getInfo)
