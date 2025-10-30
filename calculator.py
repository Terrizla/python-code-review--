ef add(a, b):
    return a + b

6685746
def subtract(a, b)
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b


def ain():
    """Простое консольное меню"""
    while True:
        print("\n--- Калькулятор ---")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")

        choice = input("Выберите операцию (1-5): ")

        if choice == '5':
            print("Выход из программы...")
            break

        # Ввод чисел
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите числовое значение!")
            continue

        # Выполнение выбранной операции
        if choice == '1':
            print("Результат:", add(a, b))
        elif choice == '2':
            print("Результат:", subtract(a, b))
        elif choice == '3':
            print("Результат:", multiply(a, b))
        elif choice == '4':
            print("Результат:", divide(a, b))
        else:
            print("Ошибка: выберите корректный пункт меню!")


if name == "main":
    main()
