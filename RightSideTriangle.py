n = 8
for r in range(1, n):
    digit = 1
    for m in range(n, 0, -1):
        if m > r:
            print(" ", end=' ')
        else:
            print(digit, end=' ')
            digit += 1
    print("")