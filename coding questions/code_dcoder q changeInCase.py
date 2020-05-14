def func1(n):
    word = input()
    lst = list(word)

    inp = input()
    inp_lst = list(inp)
    first = int(inp_lst[0])
    second = int(inp_lst[2])

    if 0 <= first <= n and 0 <= second <= n:
        if lst[first].isupper():
            lst[first] = lst[first].lower()
        elif lst[first].islower():
            lst[first] = lst[first].upper()

        if lst[second].islower():
            lst[second] = lst[second].upper()
        elif lst[second].isupper():
            lst[second] = lst[second].lower()

        str = ""
        for i in lst:
            str += i

        print(str)
    else:
        pass


n = int(input())
if 1 <= n <= 40:
    func1(n)
else:
    pass

