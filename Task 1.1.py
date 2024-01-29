def fill_dictionary():
    dictionary = {}
    while True:
        print("1. Додати елемент до словника")
        print("2. Пошук за ключем")
        print("3. Пошук за значенням")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            key = input("Введіть ключ: ")
            value = input("Введіть значення: ")
            dictionary[key] = value
            print(f"Елемент {key}: {value} додано до словника.")
        elif choice == '2':
            search_key = input("Введіть ключ для пошуку: ")
            if search_key in dictionary:
                print(f"Знайдено: {search_key}: {dictionary[search_key]}")
            else:
                print(f"Ключ {search_key} відсутній в словнику.")
        elif choice == '3':
            search_value = input("Введіть значення для пошуку: ")
            if search_value in dictionary.values():
                found_keys = [key for key, value in dictionary.items() if value == search_value]
                print(f"Знайдено за значенням {search_value}: {', '.join(found_keys)}")
            else:
                print(f"Значення {search_value} відсутнє в словнику.")
        elif choice == '0':
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    fill_dictionary()