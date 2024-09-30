from pydantic import BaseModel
from .product import Product


class Catalog(BaseModel):
    items: dict[int, Product] = {}

    def __str__(self):
        return self.model_dump_json(indent=4)