def palindome_number(n):
    if n == 0:
        return 1
    t = abs(n)
    res = 0
    while t > 0:
        ld = t % 10
        res = res * 10+ld
        t = t//10
    return n == res
n = int(input("Enter a number: "))
print(palindome_number(n))