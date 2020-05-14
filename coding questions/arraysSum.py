n = int(input())
inp = input()
lst = inp.split(' ')
print(lst)
new_lst = []
for i in lst:
    new_lst.append(int(i))
temp = new_lst[0]
summ = 0
for i in new_lst:
    if temp < i:
        temp = i
    summ += i
print(temp)
print(summ)
print(summ % temp)