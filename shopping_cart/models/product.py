from pydantic import BaseModel
from math import ceil


class Product(BaseModel):
    name: str
    icon: str
    cost: int
    revenue: float
    tax: float

    @property
    def price_per_unit(self):
        return ceil(self.cost * (1 + self.revenue))

    @property
    def final_price(self):
        return ceil(ceil(self.cost * (1 + self.revenue)) * (1 + self.tax))
