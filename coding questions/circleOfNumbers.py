n = input()
index = n.find(' ')
main_temp = int(n[:index])
temp = int(n[index + 1:])
print((temp + (main_temp // 2)) % main_temp)

# print(int((int(lst[2]) + (int(lst[0]) / 2)) % int(lst[0])))
