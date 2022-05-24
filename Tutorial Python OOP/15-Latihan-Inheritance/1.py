class Hero:
   __jumlah=0
   
   def __init__(self,name,health,attackPower,arrmor):
      self.__name = name
      self.__healthBase=health
      self.__attackPowerBase=attackPower
      self.__arrmorBase=arrmor
      self.__level=1
      self.__exp=0
      
      self.__healthMax=self.__healthBase*self.__level
      self.__attackPower=self.__attackPowerBase*self.__level
      self.__arrmor=self.__arrmorBase*self.__level
      
      self.__health=self.__healthMax
      
      Hero.__jumlah+=1
   
   @property
   def info(self):
      return "{} : \n\tLevel = {} \n\tHealth = {}/{} \n\tAttack Power = {} \n\tArrmor = {} ".format(
         self.__name,
         self.__level,
         self.__health,
         self.__healthMax,
         self.__attackPower,
         self.__arrmor
         )
         
   @property
   def gainExp(self):
      pass
   
   @gainExp.setter
   def gainExp(self,up):
      self.__exp+=up
      if self.__exp>=100:
         print("Level up")
         self.__level+=1
         self.__exp-=100
         
         self.__healthMax=self.__healthBase*self.__level
         self.__attackPower=self.__attackPowerBase*self.__level
         self.__arrmor=self.__arrmorBase*self.__level
         
         self.__health=self.__health+(self.__health*0.8)
         
   def serang(self,enemy):
      self.gainExp=25
      
# main program
shen=Hero("Shen",193,12,4)
hecraim=Hero("Hecraim",193,12,4)
   
print(shen.info)
shen.serang(hecraim)
shen.serang(hecraim)
shen.serang(hecraim)
shen.serang(hecraim)
shen.serang(hecraim)
shen.serang(hecraim)
print(shen.info)
   
   