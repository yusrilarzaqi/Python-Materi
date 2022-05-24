class Hero():
  def __init__(self, n):
    self.name = n
    
class Hero_tank(Hero):
  pass

class Hero_carry(Hero):
  pass


Shen = Hero("Shen")
Maokai = Hero_tank("Maokai")
Varus = Hero_carry("Varus")