def func1():
    cost = int(input())
    if 1 <= cost <= 100000:
        if cost > 1000:
            globals()['result'].append(cost - (cost * 0.1))
        else:
            globals()['result'].append(float(cost))


result = []
t = int(input())
if 1 <= t <= 100:
    for i in range(t):
        func1()
    for i in range(len(result)):
        print("{:.2f}".format(result[i]))