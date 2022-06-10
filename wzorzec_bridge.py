class Character:
    def __init__(self, experience, health, damage):
        self.experience = experience
        self.health = health
        self.damage = damage
    def create(self):
        print(self.__class__.__name__)
        print(self.experience, self.health, self.damage)

class FirstCharacter(Character):
    pass
class SecondCharacter(Character):
    pass

class ABC(FirstCharacter):
    def __init__(self, experience, health, damage):
        self.experience = experience
        self.health = health
        self.damage = damage
class DEF(SecondCharacter):
    def __init__(self, experience, health, damage):
        self.experience = experience
        self.health = health
        self.damage = damage

class Fabric:
    def createFirstCharacter(experience, health, damage):
        return ABC(experience, health, damage)
    def createSecondCharacter(experience, health, damage):
        return DEF(experience, health, damage)

class FirstFabric(Fabric):
    createFirstCharacter = Fabric.createFirstCharacter(0, 100, 10)
    createSecondCharacter = Fabric.createSecondCharacter(0, 100, 10)
class SecondFabric(Fabric):
    createFirstCharacter = Fabric.createFirstCharacter(0, 100, 20)
    createSecondCharacter = Fabric.createSecondCharacter(0, 100, 20)

if __name__ == '__main__':
    firstFabric = FirstFabric
    secondFabric = SecondFabric
    firstABC = firstFabric.createFirstCharacter
    secondABC = secondFabric.createSecondCharacter
    firstDEF = firstFabric.createFirstCharacter
    secondDEF = secondFabric.createSecondCharacter
    firstABC.create()
    secondABC.create()
    firstDEF.create()
    secondDEF.create()