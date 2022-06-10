from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    def __init__(self):
        self.id = None
    def set_id(self, id):
        self.id = id
    @abstractmethod
    def clone(self):
        pass
class PrototypeZ(Prototype):
    def __init__(self):
        super().__init__()
    def clone(self):
        return copy.deepcopy(self)
class PrototypeX(Prototype):
    def __init__(self):
        super().__init__()
    def clone(self):
        return copy.copy(self)

prototypez = PrototypeZ()
prototypez.set_id("1")
clonez = prototypez.clone()
prototypex = PrototypeX()
prototypex.set_id("2")
clonex = prototypex.clone()
print(f"Clones Z ID: {clonez.id}, Clones X ID: {clonex.id}")