from src.item import Item


class MixinLanguage:
    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Меняет атрибут language(язык раскладки языка)
        """
        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, MixinLanguage):
    """
        Класс содержит все атрибуты класса 'Item', и доп атрибут lenguage(EN,RU)
        имеет метод изменения языка раскладки клавиатуры.
            """

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)
