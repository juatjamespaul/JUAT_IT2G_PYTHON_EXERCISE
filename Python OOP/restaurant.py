class Restaurant:

    def __init__(
        self,
        name,
        address,
        discount_rate,
        receipt_width
    ):
        self.name = name
        self.address = address
        self.discount_rate = discount_rate
        self.receipt_width = receipt_width

        self.menu = {
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

        self.orders = []

        self.subtotal = 0.0

        self.discount = 0.0

        self.total = 0.0

    # Display Menu
    def display_menu(self):

        print("=" * self.receipt_width)

        print(
            f"{self.name:^{self.receipt_width}}"
        )

        print("=" * self.receipt_width)

        print(
            f"{'MENU':^{self.receipt_width}}"
        )

        print("-" * self.receipt_width)

        for item_name, price in self.menu.items():

            print(
                f"{item_name:<20}"
                f"P{price:>7.2f}"
            )

        print("=" * self.receipt_width)

    # Yes / No
    def ask_yes_no(self, question):

        while True:

            answer = input(
                f"{question} (y/n): "
            ).strip().lower()

            if answer in ("y", "yes"):
                return True

            if answer in ("n", "no"):
                return False

            print(
                "Invalid input. "
                "Please enter y or n."
            )

    # Get Item
    def get_item(self):

        while True:

            item_name = input(
                "  Item name: "
            ).strip().title()

            if item_name in self.menu:
                return item_name

            print(
                "Item not found. "
                "Please try again."
            )

    # Get Quantity
    def get_quantity(self):

        while True:

            quantity = input(
                "  Quantity: "
            ).strip()

            if (
                quantity.isdigit()
                and int(quantity) > 0
            ):
                return int(quantity)

            print(
                "Invalid quantity."
            )

    # Take Orders
    def take_orders(self):

        while True:

            print("\n--- New Item ---")

            item_name = self.get_item()

            quantity = self.get_quantity()

            self.orders.append(
                [item_name, quantity]
            )

            print(
                f"Added: {quantity} x {item_name}"
            )

            if not self.ask_yes_no(
                "Order another item?"
            ):
                break

    # Calculate Subtotal
    def calculate_subtotal(self):

        self.subtotal = 0.0

        for item_name, quantity in self.orders:

            self.subtotal += (
                self.menu[item_name] * quantity
            )

    # Apply Discount
    def apply_discount(self):

        eligible = self.ask_yes_no(
            "\nAre you a Senior Citizen or PWD?"
        )

        if not eligible:

            self.discount = 0.0

            return

        id_number = input(
            "Please enter your Senior Citizen/PWD ID number: "
        ).strip()

        if id_number == "":

            print("Invalid ID number.")

            self.discount = 0.0

            return

        self.discount = (
            self.subtotal
            * self.discount_rate
        )

        print(
            f"ID {id_number} verified."
        )

        print(
            f"{self.discount_rate * 100:.0f}% "
            "discount applied."
        )

    # Calculate Total
    def calculate_total(self):

        self.total = (
            self.subtotal
            - self.discount
        )

    # Print Receipt
    def print_receipt(self):

        print()

        print("=" * self.receipt_width)

        print(
            f"{self.name:^{self.receipt_width}}"
        )

        print(
            f"{self.address:^{self.receipt_width}}"
        )

        print("=" * self.receipt_width)

        print(
            f"{'ITEM':<18}"
            f"{'QTY':>5}"
            f"{'PRICE':>9}"
            f"{'TOTAL':>10}"
        )

        print("-" * self.receipt_width)

        for item_name, quantity in self.orders:

            price = self.menu[item_name]

            line_total = (
                price * quantity
            )

            print(
                f"{item_name:<18}"
                f"{quantity:>5}"
                f"{price:>9.2f}"
                f"{line_total:>10.2f}"
            )

        print("-" * self.receipt_width)

        print(
            f"{'Subtotal:':<20}"
            f"P{self.subtotal:>9.2f}"
        )

        if self.discount > 0:

            print(
                f"{'Discount:':<20}"
                f"-P{self.discount:>8.2f}"
            )

        print("-" * self.receipt_width)

        print(
            f"{'TOTAL:':<20}"
            f"P{self.total:>9.2f}"
        )

        print("=" * self.receipt_width)

        print(
            f"{'Thank you, come again!':^{self.receipt_width}}"
        )

        print("=" * self.receipt_width)

    # Run Program
    def run(self):

        self.display_menu()

        wants_to_order = self.ask_yes_no(
            "\nWould you like to order?"
        )

        if not wants_to_order:

            print(
                "\nThank you for visiting. Goodbye!"
            )

            return

        self.take_orders()

        self.calculate_subtotal()

        self.apply_discount()

        self.calculate_total()

        self.print_receipt()