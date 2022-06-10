from abc import ABC, abstractmethod

class Flyweight(QWE):
    @abstractmethod
    def justMethod(externalData: int):
        raise NotImplementedError
class xFlyweight(Flyweight):
    def justMethod(externalData: int):
        print(f"flyweight: {externalData}")
class FabricFlyweight:
    def __init__(self):
        self.fly = {}

    def fabricFlyweight(self):
        self.fly["Z"] = xFlyweight
        self.fly["X"] = xFlyweight
        self.fly["C"] = xFlyweight
    def getFlyweight(self, key: str) -> Flyweight:
        return self.fly[key]

if __name__ == '__main__':
    externalData = 63
    fabric = FabricFlyweight()
    fabric.fabricFlyweight()
    fz = fabric.getFlyweight("Z")
    fz.firstMethod(externalData - 1)
    fx = fabric.getFlyweight("X")
    fx.justMethod(externalData - 2)
    fc = fabric.getFlyweight("C")
    fc.justMethod(externalData - 3)