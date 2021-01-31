

def func1(n):
    inp = input()
    lst = inp.split(' ')
    new_lst = []
    for i in lst:
        new_lst.append(int(i))
    new_lst.sort(reverse=True)
    temp = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if temp < abs(new_lst[i] - new_lst[j]):
                temp = abs(new_lst[i] - new_lst[j])

    print(temp)


n = int(input())
if 2 <= n <= 1000:
    func1(n)
else:
    pass