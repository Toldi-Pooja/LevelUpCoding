def armstrong(num):
    if num == 0:
        return 0
    n = len(str(num))
    k = abs(num)
    res = 0
    while k > 0:
        ld = k % 10
        res = res + ld ** n
        k//=10
    return num == res
n = int(input("Enter the number: "))
print(armstrong(n))