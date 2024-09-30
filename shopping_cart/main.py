from pathlib import Path
from models import Catalog, Cart, ItemNotInCart, InvalidDiscountCode

COLOUR_OKGREEN, COLOUR_WARNING, COLOUR_END = "\033[92m", "\033[93m", "\033[0m"
def main():
    
    root_path = Path(__file__).parent

    with open(root_path / "products" / "catalog.json", "r", encoding="utf-8") as file:
        catalog = Catalog.model_validate_json(file.read())

    cart = Cart()
    while user_choice:=input("1. Add an item\n2. Remove an item\n3. Add discount code\nWhat do you want to do? "):
        
        if user_choice == "1":
            print(f"{COLOUR_OKGREEN}Add an item{COLOUR_END}")
            while product_choice := input("\n".join([f'{id}. {item.name}' for id, item in catalog.items.items()]) + "\nWhat would you like to add? "):
                if not product_choice.isdigit() or not 1 <= int(product_choice) <= len(catalog.items.values()):
                    print(f"{COLOUR_WARNING}'{product_choice}' is not a valid product selection.{COLOUR_END}")
                    continue 
                else:   
                    cart.add_item(catalog.items[int(product_choice)])
                    print(cart)
                    break

        elif user_choice == "2":
            print(f"{COLOUR_OKGREEN}Remove an item{COLOUR_END}")
            while product_choice := input("\n".join([f'{id}. {item.name}' for id, item in catalog.items.items()]) + "\nWhat would you like to remove? "):
                if not product_choice.isdigit() or not 1 <= int(product_choice) <= len(catalog.items.values()):
                    print(f"{COLOUR_WARNING}'{product_choice}' is not a valid product selection.{COLOUR_END}")
                    continue 
                try:
                    cart.remove_item(catalog.items[int(product_choice)])
                    print(cart)
                except ItemNotInCart:
                    print(f"{COLOUR_WARNING}There is no '{catalog.items[int(product_choice)].name}' in the cart to remove.{COLOUR_END}")
                break

        elif user_choice == "3":
            print(f"{COLOUR_OKGREEN}Add a discount code{COLOUR_END}")
            discount_code = input("\nCode: ")
            try:
                cart.add_discount_code(discount_code)
                print(cart)
            except InvalidDiscountCode:
                print(f"{COLOUR_WARNING}'{discount_code}' is not a valid discount code.{COLOUR_END}")
        else:
            print(f"{COLOUR_WARNING}'{user_choice}' is not a valid menu selection.{COLOUR_END}")
            continue
        



if __name__ == "__main__":
    main()

