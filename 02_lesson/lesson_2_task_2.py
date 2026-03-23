year = int(input("Введите год: "))
def is_year_leap():
        return True if year % 4 == 0 else False
result = is_year_leap()
print(f"Год {year}: {result}")

