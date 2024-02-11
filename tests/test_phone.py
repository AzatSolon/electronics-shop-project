from src.phone import Phone
from src.item import Item
import pytest


@pytest.fixture
def test_item1():
    return Item("Смартфон", 10000, 10)


@pytest.fixture
def product():
    return Phone("Фонарик", 100, 10, 1)


def test_phonerepr(product):
    assert repr(product) == "Phone('Фонарик', 100, 10, 1)"
    assert product.number_of_sim == 1


def test_phonestr(product):
    assert str(product) == "Фонарик"
