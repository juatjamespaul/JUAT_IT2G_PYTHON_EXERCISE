from restaurant import Restaurant


RESTAURANT_NAME = "JPJ Food House"
RESTAURANT_ADDRESS = "City of Naga, Cebu"
DISCOUNT_RATE = 0.30
RECEIPT_WIDTH = 30


def main():

    restaurant = Restaurant(
        RESTAURANT_NAME,
        RESTAURANT_ADDRESS,
        DISCOUNT_RATE,
        RECEIPT_WIDTH
    )

    restaurant.run()


if __name__ == "__main__":
    main()
    