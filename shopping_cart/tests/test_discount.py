from shopping_cart.models.product import Product
from shopping_cart.models.cart import Cart, InvalidDiscountCode
from pytest import fixture, raises


@fixture
def iceberg() -> Product:
    return Product(name="Iceberg", icon="🥬", cost=155, revenue=0.15, tax=0.21)


@fixture
def tomato() -> Product:
    return Product(name="Tomato", icon="🍅", cost=52, revenue=0.15, tax=0.21)


@fixture
def chicken() -> Product:
    return Product(name="Chicken", icon="🍗", cost=134, revenue=0.12, tax=0.21)


@fixture
def bread() -> Product:
    return Product(name="Bread", icon="🍞", cost=71, revenue=0.12, tax=0.1)


@fixture
def corn() -> Product:
    return Product(name="Corn", icon="🌽", cost=121, revenue=0.12, tax=0.1)


def test_no_discount(capfd, iceberg):
    cart = Cart()
    cart.add_item(iceberg)
    print(cart)
    out, _ = capfd.readouterr()
    assert out == (
        "--------------------------------------------\n"
        "| Product name | Price with VAT | Quantity |\n"
        "| -----------  | -------------- | -------- |\n"
        "| Iceberg 🥬   | £         2.17 |        1 |\n"
        "|------------------------------------------|\n"
        "| Promotion:                               |\n"
        "|------------------------------------------|\n"
        "| Total products:                        1 |\n"
        "| Total price: £                      2.17 |\n"
        "--------------------------------------------\n"
    )


def test_promo5_discount(capfd, iceberg, tomato, chicken, bread, corn):
    cart = Cart()
    cart.add_item(iceberg)
    cart.add_item(iceberg)
    cart.add_item(iceberg)
    cart.add_item(tomato)
    cart.add_item(chicken)
    cart.add_item(bread)
    cart.add_item(bread)
    cart.add_item(corn)
    cart.add_discount_code("PROMO_5")
    print(cart)
    out, _ = capfd.readouterr()
    assert out == (
        "--------------------------------------------\n"
        "| Product name | Price with VAT | Quantity |\n"
        "| -----------  | -------------- | -------- |\n"
        "| Iceberg 🥬   | £         2.17 |        3 |\n"
        "| Tomato 🍅    | £         0.73 |        1 |\n"
        "| Chicken 🍗   | £         1.83 |        1 |\n"
        "| Bread 🍞     | £         0.88 |        2 |\n"
        "| Corn 🌽      | £         1.50 |        1 |\n"
        "|------------------------------------------|\n"
        "| Promotion:      5% off with code PROMO_5 |\n"
        "|------------------------------------------|\n"
        "| Total products:                        8 |\n"
        "| Total price: £                     11.71 |\n"
        "--------------------------------------------\n"
    )


def test_promo10_discount(capfd, iceberg, tomato, chicken, bread, corn):
    cart = Cart()
    cart.add_item(iceberg)
    cart.add_item(iceberg)
    cart.add_item(iceberg)
    cart.add_item(tomato)
    cart.add_item(chicken)
    cart.add_item(bread)
    cart.add_item(bread)
    cart.add_item(corn)
    cart.add_discount_code("PROMO_10")
    print(cart)
    out, _ = capfd.readouterr()
    assert out == (
        "--------------------------------------------\n"
        "| Product name | Price with VAT | Quantity |\n"
        "| -----------  | -------------- | -------- |\n"
        "| Iceberg 🥬   | £         2.17 |        3 |\n"
        "| Tomato 🍅    | £         0.73 |        1 |\n"
        "| Chicken 🍗   | £         1.83 |        1 |\n"
        "| Bread 🍞     | £         0.88 |        2 |\n"
        "| Corn 🌽      | £         1.50 |        1 |\n"
        "|------------------------------------------|\n"
        "| Promotion:    10% off with code PROMO_10 |\n"
        "|------------------------------------------|\n"
        "| Total products:                        8 |\n"
        "| Total price: £                     11.10 |\n"
        "--------------------------------------------\n"
    )


def test_invalid_discount_code(capfd):
    cart = Cart()
    with raises(InvalidDiscountCode) as e:
        cart.add_discount_code("PROMO_100")
    assert e.match("PROMO_100 is not a valid discount code")
