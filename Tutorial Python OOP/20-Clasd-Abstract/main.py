from abc import ABC, abstractmethod

# Blue print dari class tombol lainya
class Button(ABC):
    @abstractmethod
    def click(self):
        pass


class PushButton(Button):
    def click(self):
        print("Push Button click")


tombol = PushButton()
tombol.click()
