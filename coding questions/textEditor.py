
def func1(n):
    lst = []
    for i in range(n):
        lst.append(input())
    for i in range(n):
        lst[i] = lst[i].upper()
        print(lst[i])


n = int(input())
if 1 <= n <= 100:
    func1(n)
else:
    pass