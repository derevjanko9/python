from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, parameter):
        self.parameter = parameter
        self.name = None

    def __call__(self):
        print(f'Название одежды: {self.name}')

    @abstractmethod
    def my_method(self):
        pass


class Coat(Clothes):
    @property
    def my_method(self):
        v = self.parameter
        fabric_consumption = v / 6.5 + 0.5
        return fabric_consumption


class Suit(Clothes):
    @property
    def my_method(self):
        h = self.parameter
        fabric_consumption = 2 * h + 0.3
        return fabric_consumption


coat_1 = Coat(64)
coat_1.name = 'в'
coat_1.__call__()
print(coat_1.my_method)
suit_1 = Suit(70)
suit_1.name = 'ы'
suit_1.__call__()
print(suit_1.my_method)
