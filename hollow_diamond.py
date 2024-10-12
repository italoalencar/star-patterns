n = 5

for i in range(n):
    for j in range(n - 1):
        if j == (n - 1) - i:
            print("*", end="")
        else:
            print(" ", end="")

    if i == 0:
        print("*", end="")
    else:
        print(" ", end="")

    for k in range(n - 1):
        if k == i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


for i in range(n - 1):
    for j in range(n - 1):
        if j == i + 1:
            print("*", end="")
        else:
            print(" ", end="")

    if i == n - 2:
        print("*", end="")
    else:
        print(" ", end="")

    for k in range(n - 2):
        if k == n - 3 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
