class Singleton(type):
    _inst = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._inst[cls]
class Program(metaclass=Singleton):
    pass
proA = Program()
proB = Program()
print(proA is proB)