import math

def min_boxes(n):
        return math.ceil(n / 5)
n = int(input("Ведите количество предметов:"))
print(f"минимальное количество коробок для {n} предметов:{min_boxes(n)}")

