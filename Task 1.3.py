def add_student(groups, group_name, student_name):
    if group_name not in groups:
        groups[group_name] = [student_name]
        print(f"Студент {student_name} доданий до нової групи {group_name}.")
    else:
        groups[group_name].append(student_name)
        print(f"Студент {student_name} доданий до існуючої групи {group_name}.")


def remove_student(groups, group_name, student_name):
    if group_name in groups:
        if student_name in groups[group_name]:
            groups[group_name].remove(student_name)
            print(f"Студент {student_name} видалений з групи {group_name}.")
        else:
            print(f"Студента {student_name} немає в групі {group_name}.")
    else:
        print(f"Групи {group_name} не існує.")


def display_groups(groups):
    print("Список груп та студентів:")
    for group, students in groups.items():
        print(f"{group}: {', '.join(students)}")


def main():
    groups = {}

    while True:
        print("\n1. Додати студента до групи")
        print("2. Видалити студента з групи")
        print("3. Вивести список груп та студентів")
        print("0. Вийти")

        choice = input("Ваш вибір: ")

        if choice == '1':
            group_name = input("Введіть назву групи: ")
            student_name = input("Введіть ім'я студента: ")
            add_student(groups, group_name, student_name)
        elif choice == '2':
            group_name = input("Введіть назву групи: ")
            student_name = input("Введіть ім'я студента: ")
            remove_student(groups, group_name, student_name)
        elif choice == '3':
            display_groups(groups)
        elif choice == '0':
            break
        else:
            print("Невірний вибір. Будь ласка, виберіть опцію від 1 до 4.")


if __name__ == "__main__":
    main()