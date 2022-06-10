from abc import ABC, abstractmethod

class Implementation(ABC):
    @abstractmethod
    def implementationMethod():
        raise NotImplementedError

class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation
    def setImplementation(self, value):
        self.implementation = value
    def implementationMethod(self):
        self.implementation.implementationMethod()
class DerAbstraction(Abstraction):
    def implementationMethod(self):
        self.implementation.implementationMethod()
class ExampleImplementation(Implementation):
    def implementationMethod():
        print("ExampleImplementation ImplementationMethod")
class ABCImplementation(Implementation):
    def implementationMethod():
        print("ABCImplementation ImplementationMethod")

if __name__=='__main__':
    ab = DerAbstraction(Abstraction)
    ab.setImplementation(ABCImplementation)
    ab.implementationMethod()
    ab.setImplementation(ExampleImplementation)
    ab.implementationMethod()