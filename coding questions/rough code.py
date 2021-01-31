a= 5
b= 6
print(ord('1'))
print(type(b))
if isinstance(a, int):
    print("YES")
else:
    print("isnt working")

a = [2, 4, 1, 3]

for i in range(len(a) - 1):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i], a[j] = a[j], temp

print(a)