def func1(n):
    str = input()
    lst = str.split(' ')
    for i in range(n):
        if lst[i] == 'Nemo':
            print(i+1)


n = int(input())
if 1 <= n <= 1000:
    func1(n)
else:
    pass
