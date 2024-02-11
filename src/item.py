import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_cost = self.price * self.quantity
        return total_cost

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        name getter
        """
        return self.__name

    @name.setter
    def name(self, newname):
        """
        name setter < 10 символов
        """
        if len(newname) <= 10:
            self.__name = newname
            print(f'Корректное название - {newname}')
        else:
            self.__name = newname[:10]
            print(f'Длина наименования товара превышает 10 символов - {newname[:10]}')

    @classmethod
    def instantiate_from_csv(cls, file_path) -> None:
        """
        инициализирующий экземпляры класса Item данными из файла src/items.csv
        """
        cls.all.clear()
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in list(reader):
                name = str(row['name'])
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(name):
        """
        Возвращает число из числа-строки
        """
        return int(float(name))

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        """
        Сложение класса Item как родительского с дочерними
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        else:
            return self.quantity + other.quantity
