import pytest

from src.item import Item
from src.phone import Phone


class Dog:
    def __init__(self, name: str, years_old: int):
        self.name = name
        self.years_old = years_old


@pytest.fixture
def dog():
    return Dog("Spot", 3)


@pytest.fixture
def product_phone():
    return Phone("Iphone 10", 30000, 15, 2)


@pytest.fixture
def product():
    return Item("Фонарик", 100, 10)


def test_item_init(product):
    assert product.name == "Фонарик"
    assert product.price == 100
    assert product.quantity == 10


def test_calculate_total_price(product):
    assert product.calculate_total_price() == 1000


def test_apply_discount(product):
    Item.pay_rate = 0.5
    product.apply_discount()
    assert product.price == 50.0


def test_instantiate_from_csv_none_file():
    with pytest.raises(FileNotFoundError):
        filename = 'item.csv'
        Item.instantiate_from_csv(filename)


def test_string_to_number_with_integer():
    string = "10"
    expected_result = 10
    result = Item.string_to_number(string)
    assert result == expected_result


def test_string_to_number_with_float():
    string = "3.14"
    expected_result = 3
    result = Item.string_to_number(string)
    assert result == expected_result


def test_string_to_number_with_invalid_string():
    string = "abc"
    with pytest.raises(ValueError):
        Item.string_to_number(string)


def test_repr(product):
    assert repr(product) == "Item('Фонарик', 100, 10)"


def test_str(product):
    assert str(product) == "Фонарик"


def test_add(product, product_phone, dog):
    assert product + product_phone == 25
    with pytest.raises(TypeError):
        product_phone + dog


def test_name(product):
    product.name = "12342456Суперсмарт"
    assert product.name == "12342456Су"
    product.name = "Звонилка"
    assert product.name == "Звонилка"
