def register_user(users):
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")

    if username not in users:
        users[username] = password
        print("Реєстрація успішна.")
    else:
        print("Користувач з таким іменем вже існує.")


def login_user(users):
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")

    if username in users and users[username] == password:
        print("Вхід успішний.")
    else:
        print("Неправильне ім'я користувача або пароль.")


def logout_user():
    print("Вихід з системи.")


def main():
    users = {}

    while True:
        print("\n1. Реєстрація нового користувача")
        print("2. Вхід в систему")
        print("0. Вихід з системи")

        choice = input("Ваш вибір: ")

        if choice == '1':
            register_user(users)
        elif choice == '2':
            login_user(users)
        elif choice == '0':
            logout_user()
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть опцію від 1 до 0.")


if __name__ == "__main__":
    main()