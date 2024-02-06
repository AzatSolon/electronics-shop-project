import pytest

from src.item import Item


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
