from abc import ABC, abstractmethod


class GarmentsAbstractClass(ABC):
    garmet_count = 0

    @abstractmethod
    def __init__(self, any_params):
        self.any_params = any_params
        GarmentsAbstractClass.garmet_count += 1


class Coat(GarmentsAbstractClass):

    def __init__(self, any_size):
        self.any_size = any_size

    @property
    def material_cons(self):
        material_cons = (self.any_size / 6.5) + 0.5
        return material_cons


class Suit(GarmentsAbstractClass):

    def __init__(self, any_height):
        self.any_height = any_height

    @property
    def material_cons(self):
        material_cons = (self.any_height * 2) + 0.3
        return material_cons


a = Coat(52)
print(a.material_cons)
b = Suit(183)
print(b.material_cons)
