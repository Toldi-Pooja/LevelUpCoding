#Brute force approach
"""def print_factors(n):
    if n == 0:
        return 0
    res = [ ]
    for i in range(1,n+1):
        if n % i == 0 :
            res.append(i)
    return res
n = int(input("Enter number: "))
print(print_factors(n))"""

#Better approach 
"""def factors(n):
    if n == 0:
        return 0
    res = []
    for i in range(1,n//2):
        if n % i == 0:
            res.append(i)
    res.append(n)
    return res
n = int(input("Enter number: "))
print(factors(n))"""

#Optimal approach
from math import sqrt
def factors(n):
    if n == 0:
        return 0
    res = []
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            res.append(i)
            if n//i !=i:
                res.append(n//i)
    res.sort()
    return res
n = int(input())
print(factors(n))