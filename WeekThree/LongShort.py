def longShort(string):
    return "Long" if len(string) > 10 else "Short"
s = input()
print(longShort(s))