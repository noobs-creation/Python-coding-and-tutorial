n = int(input())
inp = input()
lst_temp = list(inp)
print(lst_temp)

lst = []
for i in lst_temp:
    if i != ' ':
        lst.append(int(i))
print(lst)
lst = lst[::-1]
print(lst)