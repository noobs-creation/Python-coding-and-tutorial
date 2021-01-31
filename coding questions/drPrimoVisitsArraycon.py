import math


def isPrime_V3(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n > 2 and n % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for i in range(3, max_divisor + 1, 2):
        if n % i == 0:
            return False
    return True


n = int(input())
inp = input()
lst = inp.split(' ')

count = 0
for i in range(n):
    if isPrime_V3(int(lst[i])):
        count += 1

print(count)