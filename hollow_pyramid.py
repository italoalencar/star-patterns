n = 5

for i in range(n):
    for j in range(n - 1):
        if j == (n - 1) - i or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    if i == 0 or i == n - 1:
        print("*", end="")
    else:
        print(" ", end="")

    for k in range(n - 1):
        if k == i - 1 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")

    print()
