
def func1(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end="")
            if j != i:
                print(" ", end="")
        print()

n = int(input())
if 1 <= n <= 9:
    func1(n)
else:
    pass