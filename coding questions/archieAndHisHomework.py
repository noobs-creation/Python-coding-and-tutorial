# Function to find HCF the Using Euclidean algorithm
def compute_hcf(x, y):
    while y:
        x, y = y, x % y
    return x


inp = input()
lst = inp.split(" ")
numerator = int(lst[0])
denominator = int(lst[1])

if 1 <= numerator <= denominator <= 1000:
    temp = compute_hcf(numerator, denominator)
    print("{} {}".format(numerator // temp, denominator // temp))
else:
    pass
