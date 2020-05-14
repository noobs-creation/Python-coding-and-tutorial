n = int(input())
if 1 <= n <= 26:

    for i in range(n+96, 96, -1):
        print(chr(i), end="")

else:
    pass