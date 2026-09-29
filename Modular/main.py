from menu import display_menu
from orders import ask_yes_no, take_orders
from payment import calculate_subtotal, apply_discount
from receipt import print_receipt


RESTAURANT_NAME = "JPJ Food House"
RESTAURANT_ADDRESS = "City of Naga, Cebu"
DISCOUNT_RATE = 0.30
RECEIPT_WIDTH = 30

menu = {
    "Chicken Joy": 99.00,
    "Burger Steak": 89.00,
    "Cheeseburger": 79.00,
    "Spaghetti": 69.00,
    "Beef Tapa Rice": 95.00,
    "Fries": 49.00,
    "Lumpia (3pcs)": 45.00,
    "Soda": 35.00,
    "Iced Tea": 39.00,
    "Buko Juice": 42.00,
    "Halo-Halo": 65.00,
    "Leche Flan": 45.00
}


def main():
    display_menu(
        menu,
        RESTAURANT_NAME,
        RECEIPT_WIDTH
    )

    wants_to_order = ask_yes_no(
        "\nWould you like to order?"
    )

    if not wants_to_order:
        print("\nThank you for visiting. Goodbye!")
        return

    orders = take_orders(menu)

    subtotal = calculate_subtotal(
        orders,
        menu
    )

    discount_amount = apply_discount(
        subtotal,
        DISCOUNT_RATE
    )

    print_receipt(
        orders,
        menu,
        subtotal,
        discount_amount,
        RESTAURANT_NAME,
        RESTAURANT_ADDRESS,
        RECEIPT_WIDTH
    )


if __name__ == "__main__":
    main()