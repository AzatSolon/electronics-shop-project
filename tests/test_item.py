from src.item import Item

product = Item("Ноутбук MSI", 100000, 10)


def test_calculate_total_price():
    assert product.calculate_total_price() == 500000.0


product.pay_rate = 0.5
product.apply_discount()


def test_apply_discount():
    assert product.price == 50000.0
