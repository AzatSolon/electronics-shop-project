from src.phone import Phone
import pytest


@pytest.fixture
def product():
    return Phone("Фонарик", 100, 10, 1)


def test_phonerepr(product):
    assert repr(product) == "Phone('Фонарик', 100, 10, 1)"


def test_phonestr(product):
    assert str(product) == "Фонарик"
