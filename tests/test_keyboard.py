import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Clatz GTX13800', 10000, 8)


def test_init(keyboard):
    assert str(keyboard) == 'Clatz GTX13800'
    assert str(keyboard.language) == 'EN'
    assert str(keyboard.quantity) == '8'
    assert keyboard.price == 10000


def test_change_lang(keyboard):
    keyboard.change_lang()
    assert str(keyboard.language) == "RU"
    keyboard.change_lang()
    assert str(keyboard.language) == "EN"
