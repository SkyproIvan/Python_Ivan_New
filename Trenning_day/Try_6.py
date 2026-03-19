lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]
l = len(lst)
for n in lst:
    if (n > 10) and (n % 6 == 0):
        print(n)