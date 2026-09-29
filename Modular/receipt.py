def print_receipt(
    orders,
    menu_dict,
    subtotal,
    discount_amount,
    restaurant_name,
    restaurant_address,
    width
):
    total = subtotal - discount_amount

    print()

    print("=" * width)

    print(
        f"{restaurant_name:^{width}}"
    )

    print(
        f"{restaurant_address:^{width}}"
    )

    print("=" * width)

    print(
        f"{'ITEM':<18}"
        f"{'QTY':>5}"
        f"{'PRICE':>9}"
        f"{'TOTAL':>10}"
    )

    print("-" * width)

    for item_name, quantity in orders:

        price = menu_dict[item_name]

        line_total = price * quantity

        print(
            f"{item_name:<18}"
            f"{quantity:>5}"
            f"{price:>9.2f}"
            f"{line_total:>10.2f}"
        )

    print("-" * width)

    print(
        f"{'Subtotal:':<20}"
        f"P{subtotal:>9.2f}"
    )

    if discount_amount > 0:
        print(
            f"{'Discount:':<20}"
            f"-P{discount_amount:>8.2f}"
        )

    print("-" * width)

    print(
        f"{'TOTAL:':<20}"
        f"P{total:>9.2f}"
    )

    print("=" * width)

    print(
        f"{'Thank you, come again!':^{width}}"
    )

    print("=" * width)