def check_divisibility():
    n = int(input("Введите конец диапазона:"))
    for i in range(1,n+1):
        if i % 4 == 0:
            print(f"{i} Делится на 2 и на 4")
        elif i % 2 == 0:
            print(f"{i} Делится на 2 но не на 4")
        else:
            print(i)

check_divisibility()