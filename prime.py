import math
import time


def isPrime_V1(n):
    if n == 1:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def isPrime_V2(n):
    if n == 1:
        return False
    max_divisor = math.floor(math.sqrt(n))
    for i in range(2, max_divisor + 1):
        if n % i == 0:
            return False
    return True


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


# driver code
def main():
    n = int(input("enter a number to check it is prime or not : "))
    op = int(input(
        "enter the version you want to use for finding the answer (1 = basic, 2 = efficient, 3 = most efficient): "))

    if op == 1:
        t0 = time.time()
        if isPrime_V1(n):
            print("the number {} is prime".format(n))
        else:
            print("the number {} is not prime".format(n))
        t1 = time.time()
        print('time taken : ', t1 - t0)
    elif op == 2:
        t0 = time.time()
        if isPrime_V2(n):
            print("the number {} is prime".format(n))
        else:
            print("the number {} is not prime".format(n))
        t1 = time.time()
        print('time taken : ', t1 - t0)
    elif op == 3:
        t0 = time.time()
        if isPrime_V3(n):
            print("the number {} is prime".format(n))
        else:
            print("the number {} is not prime".format(n))
        t1 = time.time()
        print('time taken : ', t1 - t0)


main()
