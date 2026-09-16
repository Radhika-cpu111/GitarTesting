def calculate_total(price, quantity):
    return price * quantity


def main():
    price = 100
    quantity = 3

    total = calculate_total(price, quantity)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
