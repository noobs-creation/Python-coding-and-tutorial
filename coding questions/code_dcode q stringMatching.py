n = int(input())
lst = []
for i in range(n):
    lst.append(input())
for i in lst:
    index = i.find(' ')
    main_temp = i[:index]
    temp = i[index+1:]
    if temp in main_temp:
        print("Yes")
    else:
        print("No")