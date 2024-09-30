from shopping_cart.models import Product, Cart, ItemNotInCart
import pytest


@pytest.fixture
def iceberg() -> Product:
    return Product(name="Iceberg", icon="🥬", cost=155, revenue=0.15, tax=0.21)


@pytest.fixture
def tomato() -> Product:
    return Product(name="Tomato", icon="🍅", cost=52, revenue=0.15, tax=0.21)


@pytest.fixture
def chicken() -> Product:
    return Product(name="Chicken", icon="🍗", cost=134, revenue=0.12, tax=0.21)


@pytest.fixture
def bread() -> Product:
    return Product(name="Bread", icon="🍞", cost=71, revenue=0.12, tax=0.1)


@pytest.fixture
def corn() -> Product:
    return Product(name="Corn", icon="🌽", cost=121, revenue=0.12, tax=0.1)


def test_cart_add_item(iceberg):
    cart = Cart()
    assert cart.item_count == 0
    cart.add_item(iceberg)
    assert cart.item_count == 1
    cart.add_item(iceberg)
    assert cart.item_count == 2
    cart.add_item(iceberg)
    assert cart.item_count == 3


def test_cart_remove_item(iceberg):
    cart = Cart()
    assert cart.item_count == 0
    cart.add_item(iceberg)
    assert cart.item_count == 1
    cart.add_item(iceberg)
    assert cart.item_count == 2
    cart.add_item(iceberg)
    assert cart.item_count == 3
    cart.remove_item(iceberg)
    assert cart.item_count == 2
    cart.remove_item(iceberg)
    assert cart.item_count == 1

    assert "Iceberg" in cart.items
    cart.remove_item(iceberg)
    assert cart.item_count == 0
    assert "Iceberg" not in cart.items

    with pytest.raises(ItemNotInCart) as e:
        cart.remove_item(iceberg)
    assert e.match("Can not remove Iceberg from cart")


def test_print_empty_cart(capfd):
    cart = Cart()
    print(cart)
    out, _ = capfd.readouterr()
    assert out == (
        "--------------------------------------------\n"
        "| Product name | Price with VAT | Quantity |\n"
        "| -----------  | -------------- | -------- |\n"
        "|------------------------------------------|\n"
        "| Promotion:                               |\n"
        "|------------------------------------------|\n"
        "| Total products:                        0 |\n"
        "| Total price: £                      0.00 |\n"
        "--------------------------------------------\n"
    )


def test_print_cart_one_item(capfd, iceberg):
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


def test_print_cart_all_items(capfd, iceberg, tomato, chicken, bread, corn):
    cart = Cart()
    cart.add_item(iceberg)
    cart.add_item(tomato)
    cart.add_item(chicken)
    cart.add_item(bread)
    cart.add_item(corn)
    print(cart)
    out, _ = capfd.readouterr()
    assert out == (
        "--------------------------------------------\n"
        "| Product name | Price with VAT | Quantity |\n"
        "| -----------  | -------------- | -------- |\n"
        "| Iceberg 🥬   | £         2.17 |        1 |\n"
        "| Tomato 🍅    | £         0.73 |        1 |\n"
        "| Chicken 🍗   | £         1.83 |        1 |\n"
        "| Bread 🍞     | £         0.88 |        1 |\n"
        "| Corn 🌽      | £         1.50 |        1 |\n"
        "|------------------------------------------|\n"
        "| Promotion:                               |\n"
        "|------------------------------------------|\n"
        "| Total products:                        5 |\n"
        "| Total price: £                      7.11 |\n"
        "--------------------------------------------\n"
    )
