def func1(t):

    inp = input()
    lst = inp.split(' ')
    maths = int(lst[0])
    algo = int(lst[1])


    if 1 <= maths <= 100 and 1 <= algo <= 100:
        if maths > 70 and algo > 50:
            globals()['result'].append("Pass")
        else:
            globals()['result'].append("Fail")


result = []
t = int(input())
if 1 <= t <= 10:
    for i in range(t):
        func1(t)
    for i in result:
        print(i)
else:
    pass