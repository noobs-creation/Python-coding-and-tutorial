n = int(input())
if 1 <= n <= 26:
    inp = input()

    lst = inp.split(' ')

    new_lst = []
    for i in lst:
        new_lst.append(i.lower())

    for i in range(n - 1):
        for j in range(i, n):
            if new_lst[i] > new_lst[j]:
                temp = lst[i]
                lst[i], lst[j] = lst[j], temp

    for i in range(n):
        print(lst[i], end="")
        if i != n-1:
            print(" ", end="")
else:
    pass