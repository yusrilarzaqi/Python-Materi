from abc import ABC,abstractmethod

class Button(ABC):
   def __init__(self,set_link):
      self.link=self.set_link
      
   @abstractmethod
   def click(self):
      pass
   
   @property
   @abstractmethod
   def link(self):
      pass
   
class PushButton(Button):
   def click(self):
      print(f"Go To : {self.link}")
   
   @Button.link.setter
   def link(self,i):
      self.__link=i
      
   @link.getter
   def link(self):
      return self.__link
      
tombol = PushButton('google')


