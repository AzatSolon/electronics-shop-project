from src.item import Item


class Phone(Item):
    """
    Класс содержит все атрибуты класса `Item` и дополнительно атрибут, содержащий количество поддерживаемых сим-карт
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @classmethod
    def get_classname(cls):
        return cls.__name__

    def __repr__(self):
        return f"{self.get_classname()}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim):
        if sim > 0:
            self.__number_of_sim = sim
        else:
            raise ValueError('Количество SIM-карт должно быть целым числом больше нуля.')
