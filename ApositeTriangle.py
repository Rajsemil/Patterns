n = int(input("Enter a number: "))
m = 0
for i in range(n, 0, -1):
    m += 1
    for n in range(1, i + 1):
        print(m, end=' ')
    print('\r')