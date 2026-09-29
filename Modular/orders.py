def ask_yes_no(question_text):
    while True:
        answer = input(
            f"{question_text} (y/n): "
        ).strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print(
            "Invalid input. "
            "Please enter y or n."
        )


def get_valid_item(menu_dict):
    while True:
        item_name = input(
            "  Item name: "
        ).strip().title()

        if item_name in menu_dict:
            return item_name

        print(
            "Item not found on the menu. "
            "Please try again."
        )


def get_valid_quantity():
    while True:
        quantity = input(
            "  Quantity: "
        ).strip()

        if quantity.isdigit() and int(quantity) > 0:
            return int(quantity)

        print(
            "Invalid quantity. "
            "Enter a number greater than 0."
        )


def take_orders(menu_dict):
    orders = []

    while True:
        print("\n--- New Item ---")

        item_name = get_valid_item(menu_dict)

        quantity = get_valid_quantity()

        orders.append(
            [item_name, quantity]
        )

        print(
            f"Added: {quantity} x {item_name}"
        )

        if not ask_yes_no(
            "Order another item?"
        ):
            break

    return orders