n = 5

for i in range(n):
    for j in range(n - 1):
        if j < (n - 1) - i:
            print(" ", end="")
        else:
            print("*", end="")

    print("*", end="")

    for k in range(n - 1):
        if k < i:
            print("*", end="")
    print()
