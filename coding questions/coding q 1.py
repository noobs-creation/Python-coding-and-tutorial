def custom_checker(lst, n):
    for i in range(n-1):
        for j in range(i+1, n):
            pass


def main():
    n = int(input())
    lst = []
    for i in range(n):
        lst.append(input())
    custom_checker(lst, n)


main()