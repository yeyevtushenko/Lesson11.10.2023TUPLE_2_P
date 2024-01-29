import random


def generate_random_products():
    products = {}
    for _ in range(5):
        product_name = f"Product {random.randint(1, 100)}"
        product_price = round(random.uniform(10, 100), 2)
        products[product_name] = product_price
    return products


def main():
    product_dict = generate_random_products()

    while True:
        print("Список товарів та їх цін:")
        for product, price in product_dict.items():
            print(f"{product}: {price} грн")

        user_input = input("Введіть назву товару (або 'exit' для виходу): ")

        if user_input.lower() == 'exit':
            break

        if user_input in product_dict:
            print(f"Ціна товару '{user_input}': {product_dict[user_input]} грн")
        else:
            print(f"Товар '{user_input}' не знайдено.")


if __name__ == "__main__":
    main()