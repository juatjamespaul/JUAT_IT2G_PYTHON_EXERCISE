from orders import ask_yes_no


def calculate_subtotal(orders, menu_dict):
    subtotal = 0.0

    for item_name, quantity in orders:
        subtotal += (
            menu_dict[item_name] * quantity
        )

    return subtotal


def apply_discount(subtotal, discount_rate):

    eligible = ask_yes_no(
        "\nAre you a Senior Citizen or PWD?"
    )

    if not eligible:
        return 0.0

    id_number = input(
        "Please enter your Senior Citizen/PWD ID number: "
    ).strip()

    if id_number == "":
        print("Invalid ID number.")
        return 0.0

    discount = subtotal * discount_rate

    print(
        f"ID {id_number} verified."
    )

    print(
        f"{discount_rate * 100:.0f}% discount applied."
    )

    return discount