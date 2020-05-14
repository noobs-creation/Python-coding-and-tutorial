def func1(n):
    str = input()
    lst = list(str)
    for i in lst:
        new_lst = list(i)
        for j in new_lst:
            if 48 <= ord(j) <= 57:
                print(j, end=" ")


n = int(input())
if 1 <= n <= 50:
    func1(n)
