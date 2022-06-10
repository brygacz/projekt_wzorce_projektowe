class SystemA:
    def methodOne():
        print("SystemA method")
class SystemB:
    def methodTwo():
        print("SystemB method")
class SystemC:
    def methodThree():
        print("SystemC method")
class SystemD:
    def methodFour():
        print("SystemD method")
class SystemE:
    def methodFive():
        print("SystemE method")

class Facade():
    def __init__(self) -> None:
        self.first = SystemA
        self.second = SystemB
        self.third = SystemC
        self.fourth = SystemD
        self.fifth = SystemE
    def methodA(self):
        print("Method A")
        self.first.methodOne()
        self.second.methodTwo()
        self.third.methodThree()
    def metodaB(self):
        print("Method B")
        self.third.methodThree()
        self.fourth.methodFour()
if __name__ == '__main__':
    facade = Facade()
    facade.methodA()
    facade.methodB()