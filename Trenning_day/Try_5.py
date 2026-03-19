def quarter_of_year():
    n = int(input("Введите месяц: "))
    if 1 < n < 4:
        print(f"Месяц №{n} это I квартал")
    elif 3 < n < 7:
        print(f"Месяц №{n} это II квартал")
    elif 6 < n < 10:
        print(f"Месяц №{n} это III квартал")
    elif 9 < n < 13:
        print(f"Месяц №{n} это IV квартал")
    else:
        print("Введите корректное значение месяца")


quarter_of_year()