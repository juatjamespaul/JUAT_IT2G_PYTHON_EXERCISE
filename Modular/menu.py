def print_divider(width, character="="):
    print(character * width)


def display_menu(menu_dict, restaurant_name, width):
    print_divider(width)

    print(f"{restaurant_name:^{width}}")

    print_divider(width)

    print(f"{'MENU':^{width}}")

    print_divider(width, "-")

    for item_name, price in menu_dict.items():
        print(
            f"{item_name:<20}"
            f"P{price:>7.2f}"
        )

    print_divider(width)