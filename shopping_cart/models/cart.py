from pydantic import BaseModel
from .product import Product


class InvalidDiscountCode(Exception):
    """
    Exception thrown when an invalid discoutn code is entered.
    """


class ItemNotInCart(Exception):
    """
    Exception thrown when an item does not exist in the cart.
    """


class CartItem(BaseModel):
    """
    Model to represent the count of each product in the cart.
    """

    product: Product
    quantity: int


class Cart(BaseModel):
    """
    Model to represent the contents of a shopping cart.
    """

    items: dict[str, CartItem] = {}
    discount: float = 0
    discount_code: str = None

    @property
    def item_count(self) -> int:
        return sum(item.quantity for item in self.items.values())

    @property
    def total_price(self) -> float:
        """
        Returns the total price of the cart items.
        """
        return sum(
            [item.product.final_price * item.quantity for item in self.items.values()]
        )

    @property
    def total_price_with_discount(self) -> float:
        """
        Returns the total price of the cart items with any discount applied.
        """
        return sum(
            [item.product.final_price * item.quantity for item in self.items.values()]
        ) * (1 - self.discount)

    def add_item(self, item: Product, quantity: int = 1) -> None:
        """
        Add a product to the shopping cart.
        """
        if self.items.get(item.name):
            self.items[item.name].quantity += quantity
        else:
            self.items.update({item.name: CartItem(product=item, quantity=quantity)})

    def remove_item(self, item: Product, quantity: int = 1) -> None:
        """
        Remove a product from the shopping cart.
        """
        if self.items.get(item.name) and self.items[item.name].quantity > 1:
            self.items[item.name].quantity -= quantity
        elif self.items.get(item.name) and self.items[item.name].quantity == 1:
            del self.items[item.name]
        else:
            err_msg = f"Can not remove {item.name} from cart."
            raise ItemNotInCart(err_msg)

    def add_discount_code(self, discount_code: str) -> None:
        if discount_code == "PROMO_5":
            self.discount = 0.05
            self.discount_code = "PROMO_5"
        elif discount_code == "PROMO_10":
            self.discount = 0.1
            self.discount_code = "PROMO_10"
        else:
            err_msg = f"{discount_code} is not a valid discount code."
            raise InvalidDiscountCode(err_msg)

    def __str__(self) -> str:
        """
        Print a formatted summary of the cart.
        """
        summary = (
            (
                "--------------------------------------------\n"
                "| Product name | Price with VAT | Quantity |\n"
                "| -----------  | -------------- | -------- |\n"
            )
            + "".join(
                [
                    f"| {(item.product.name + ' ' + item.product.icon):11} | £ {item.product.final_price/100: >12.2f} | {item.quantity: >8} |\n"
                    for item in self.items.values()
                ]
            )
            + (
                "|------------------------------------------|\n"
                f"| Promotion: {str(int(self.discount*100)) + '% off with code ' + self.discount_code if self.discount_code else '':>29} |\n"
                "|------------------------------------------|\n"
                f"| Total products: {self.item_count: >24} |\n"
                f"| Total price: £ {self.total_price_with_discount/100: >25.2f} |\n"
                "--------------------------------------------"
            )
        )
        return summary
