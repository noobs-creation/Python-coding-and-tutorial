"""
custom encoder such that

for example :
a will become t

a + ascii of 'a' = ascii of 't'

"""


def custom_encoder(inp):
    for i in inp:
        ascii_temp = ord(i)
        temp = ascii_temp
        for j in range(ascii_temp):
            temp += 1
            if temp == 123:
                temp = 97
        print(chr(temp), end="")


def main():
    inp = input("enter text : ")
    custom_encoder(list(inp))


main()