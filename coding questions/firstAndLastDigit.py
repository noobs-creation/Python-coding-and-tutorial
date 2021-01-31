
def func1(t):
    inp = input()
    lst = list(inp)
    globals()['result'] .append(int(lst[0]) + (int(lst[len(lst)-1])))




result = []
t = int(input())
if 1 <= t <= 100:
    for i in range(t):
        func1(t)
    for i in result:
        print(i)
else:
    pass

