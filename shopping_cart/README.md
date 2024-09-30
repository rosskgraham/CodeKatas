# Shopping Cart
https://www.codurance.com/katas/shopping-cart-kata

Technical requirements
- The price per unit is calculated based on the product cost and the percentage of revenue that the company wants for that product.
- The price has to be rounded up; so if a price per unit calculated is 1.7825, then the expected price per unit for that product is 1.79
- The final price of the product is then calculated as the price per unit with the VAT rounded up.
- Products are not allowed to have the same name.

## Set up virtual environment
```powershell
PS C:\..\shopping_cart> py -m venv .venv
PS C:\..\shopping_cart> .venv\Scripts\Activate
(.venv) PS C:\..\shopping_cart> py -m pip install --upgrade pip
(.venv) PS C:\..\shopping_cart> py -m pip install poetry
(.venv) PS C:\..\shopping_cart> poetry install
```

## Tests

From the repository root

```powershell
(.venv) PS C:\..\CodeKatas> py -m pytest -s .\shopping_cart\tests\
```

## What did I learn
- Took TDD approach and wrote the tests first
- colour coding terminal text
- parsing json into pydantic model
- using @property decorator on class method
- more fstring format spec
- pytest capfd fixture to capture test stdout/stderr