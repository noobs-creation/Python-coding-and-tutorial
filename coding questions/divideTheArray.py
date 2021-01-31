
def func1(n):
    inp = input()
    lst = inp.split(' ')
    new_lst = []
    for i in lst:
        new_lst.append(int(i))

    for i in range(1, n+1):
        if i % 2 == 0:
            if new_lst[i-1] % 2 == 0:
                print(new_lst[i-1], end=' ')


n = int(input())
if 1 <= n <= 1000:
    func1(n)
else:
    pass