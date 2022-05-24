class Hero:
  def __init__(self, name, health):
    self.__name = name
    self.__health = health
  
  @property
  def info(self):
    return f'{self.__name} : \n\tHealth : {self.__health}'

  # Cara salah
  # def __init__(self, name):
  #  self.__name = name
  #  self.__health = 600
  
class Hero_tank(Hero):
  def __init__(self, name):
    # Hero.__init__(self, name, 600)
    super().__init__(name, 600)
    
class Hero_cary(Hero):
  def __init__(self, name):
    super.__init__(name, 583)
    
Shen = Hero_tank("Shen")
Samira = Hero_cary("Samira")

print(Shen.info)
print(Samira.info)