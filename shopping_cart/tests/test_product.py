from shopping_cart.models.product import Product


def test_product_iceberg():
    product = Product(name="Iceberg", icon="🥬", cost=155, revenue=0.15, tax=0.21)
    assert product.name == "Iceberg"
    assert product.icon == "🥬"
    assert product.cost == 155
    assert product.revenue == 0.15
    assert product.tax == 0.21
    assert product.price_per_unit == 179
    assert product.final_price == 217


def test_product_tomato():
    product = Product(name="Tomato", icon="🍅", cost=52, revenue=0.15, tax=0.21)
    assert product.name == "Tomato"
    assert product.icon == "🍅"
    assert product.cost == 52
    assert product.revenue == 0.15
    assert product.tax == 0.21
    assert product.price_per_unit == 60
    assert product.final_price == 73


def test_product_chicken():
    product = Product(name="Chicken", icon="🍗", cost=134, revenue=0.12, tax=0.21)
    assert product.name == "Chicken"
    assert product.icon == "🍗"
    assert product.cost == 134
    assert product.revenue == 0.12
    assert product.tax == 0.21
    assert product.price_per_unit == 151
    assert product.final_price == 183


def test_product_bread():
    product = Product(name="Bread", icon="🍞", cost=71, revenue=0.12, tax=0.1)
    assert product.name == "Bread"
    assert product.icon == "🍞"
    assert product.cost == 71
    assert product.revenue == 0.12
    assert product.tax == 0.1
    assert product.price_per_unit == 80
    assert product.final_price == 88


def test_product_corn():
    product = Product(name="Corn", icon="🌽", cost=121, revenue=0.12, tax=0.1)
    assert product.name == "Corn"
    assert product.icon == "🌽"
    assert product.cost == 121
    assert product.revenue == 0.12
    assert product.tax == 0.1
    assert product.price_per_unit == 136
    assert product.final_price == 150
