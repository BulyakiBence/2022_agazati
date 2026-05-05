def is_xxyy(n):
    ertek = n*n-1

    if 1000 <= ertek <= 9999:
        s = str(ertek)

        if s[0] == s[1] and s[2] == s[3]:
            return True
    return False

talalatok = []
for i in range (1,100):
    if is_xxyy(i):
        talalatok.append(str(i))

print(talalatok)    