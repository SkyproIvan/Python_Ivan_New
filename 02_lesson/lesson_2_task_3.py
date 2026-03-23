import math
x = float(input("Введите длину стороны: "))
def square():
    return math.ceil(x * x)
result = square()
print(f"Площадь квадрата со стороной {x} = {result}")
