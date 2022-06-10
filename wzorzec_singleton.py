from abc import ABC, abstractmethod

class Item(ABC):
    @abstractmethod
    def question():
        raise NotImplementedError
class SpecificItem(Item):
    def question():(self):
        print("SpecificItem.question()")

class Proxy(Item):
    def __init__(self):
        self.SpecificItem: SpecificItem = None
    def question(self):
        if self.specificItem is None:
            self.specificItem = SpecificItem()
        self.specificItem.question()
if __name__ == '__main__':
    proxy.question()
    proxy = Proxy()