from typing import Any
from abc import ABC, abstractmethod
from __future__ import annotations

class Builder(ABC):
    @abstractmethod
    @property
    def product(self):
        pass
    @abstractmethod
    def takePartA(self):
        pass
    @abstractmethod
    def takeBartB(self):
        pass

class BuilderAB(Builder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def takePartA(self):
        self._product.add("part A")
    def takePartB(self):
        self._product.add("part B")

class BuilderCD(Builder):
    def __init__(self):
        self.reset()
    def reset(self):
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def takePartA(self):
        self._product.add("part C")
    def takePartB(self):
        self._product.add("part D")

class Product():
    def __init__(self):
        self.parts = []
    def add(self, part: Any):
        self.parts.append(part)

    def parts_list(self):
        print(f"Products parts: {', '.join(self.parts)}", end="")

class Chief:
    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder
    @builder.setter
    def builder(self, builder: Builder):
        self._builder= builder
    def take(self):
        self.builder.takePartA()
        self.builder.takePartAB()

if __name__ == "__main__":
    chief = Chief()
    builderab = BuilderAB()
    buildercd = BuilderCD()
    chief.builder = builderef
    print("\n")
    chief.take()
    builderab.product.parts_list()
    chief.builder = buildercd
    print("\n")
    chief.take()
    buildercd.product.parts_list()