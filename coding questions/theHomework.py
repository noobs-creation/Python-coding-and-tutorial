from math import pow
def func1(t):
    for i in range(t):

        n = int(input())
        inp = input()
        lst = inp.split(" ")

        new_lst = []
        for i in lst:
            new_lst.append(int(i))
        new_lst.sort()

        max = 1
        for i in range(n-1, 0, -1):
            max += int(pow(10, i)) * new_lst[i]
        print(((max//10)*10) + new_lst[0])

n = int(input())
if 1 <= n <= 100:
    func1(n)