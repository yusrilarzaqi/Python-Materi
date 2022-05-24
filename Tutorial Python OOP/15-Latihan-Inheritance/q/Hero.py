class Hero:
   def __init__(self,name):
      self.__name=name
      self.__health_pool=[0,100,200,300,400,500]
      self.__attack_pool=[]
      self.__arrmor_pool=[]
      self.__level=0
      self.__exp=0
   
   def show_info(self):
      print("{}\tLevel : {} \n\tHealth : {} \n\tAttack : {} \n\tArrmor : {}".format(self.__name,self.__level,self.__health,self.__attack,self.__arrmor))
      
   @property
   def health_pool(self):
      pass
   
   @property
   def attack_pool(self):
      pass
   
   @property
   def arrmor_pool(self):
      pass
   
   @property
   def levelUp(self):
      pass
   
   @property
   def gainExp(self):
      pass
   
   @health_pool.setter
   def health_pool(self,i):
      self.__health_pool = i
      
   @attack_pool.setter
   def attack_pool(self,i):
      self.__attack_pool = i

   @arrmor_pool.setter
   def arrmor_pool(self,i):
      self.__arrmor_pool = i

   @gainExp.setter
   def gainExp(self,i):
      self.__exp+=i
      if self.__exp>=100:
         self.levelUp=self.__exp//100
         self.__exp%=100

   @levelUp.setter
   def levelUp(self,i):
      self.__level += i
      self.__health=self.__health_pool[self.__level]
      self.__attack=self.__attack_pool[self.__level]
      self.__arrmor=self.__arrmor_pool[self.__level]


class HeroCarry(Hero):
   def __init__(self,name):
      super().__init__(name)
      self.health_pool=[0,102,204,306,408,510]
      self.attack_pool=[0,12,24,36,48,60]
      self.arrmor_pool=[0,2,4,6,8,10]
      self.levelUp=1


class HeroTank(Hero):
   def __init__(self,name):
      super().__init__(name)
      self.health_pool=[0,110,220,330,440,550]
      self.attack_pool=[0,8,9.5,11,12.5,14]
      self.arrmor_pool=[0,10,15,20,25,30]
      self.levelUp=1


