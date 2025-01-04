n = 6 
for i in range(n, 0, -1):
    print("X" * i)

n = 6
for i in range(n, 0, -2):
    print("x" * i)
    print("-" * (i - 1))

n = 6
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

n = 6
for i in range(1, n + 1):
    print("X" * i)
for i in range(n - 1, 0, -1):
    print("X" * i)

n = 6
for i in range(n, 0, -1):
    print("." * (i - 1) + str(i))