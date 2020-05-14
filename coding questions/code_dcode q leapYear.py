n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
for i in lst:
    if i % 4 == 0:
        if i % 100 == 0 :
            if i % 400 == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")
    else:
        print("No")