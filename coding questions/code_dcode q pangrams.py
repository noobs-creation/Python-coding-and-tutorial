
def func1(str):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for ch in alphabets:
        if ch not in str.lower():
            print("NO")
            return None
    print("YES")


inp = input()
if len(inp) < 26:
    print("NO")
else:
    func1(inp)
