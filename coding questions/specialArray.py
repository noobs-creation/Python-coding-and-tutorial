def func1(n):
    inp = input()
    lst = inp.split(' ')
    new_lst = []
    for i in lst:
        new_lst.append(int(i))
    for i in new_lst:
        if i == 0:
            print("No")
            return None
    print("Yes")


n = int(input())
if 1 <= n <= 100:
    func1(n)
else:
    pass
