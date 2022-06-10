class Character:

    def __init__(self, experience, health, damage):
        self.experience = experience
        self.health = health
        self.damage = damage

    def create(self):
        print(self.__class__.__name__)
        print(self.experience, self.health, self.damage)

class Maverick(Jednostka):
    def __init__(self):
        self.experience = 0
        self.health = 250
        self.damage = 55


class Assasin(Character):
    def __init__(self):
        self.experience = 0
        self.health = 100
        self.damage = 10

def fabric(character=""):
    characters = {
        "Maverick": Maverick,
        "Assasin": Assasin}
    return characters[character]()
if __name__ == '__main__':
    maverick = fabric("Maverick")
    assasin = fabric("Assasin")


    print(maverick.create())
    print(assasin.create())