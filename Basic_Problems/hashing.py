def hashing(n,m):
    hash_list = [0]*11
    for num in n:
        hash_list[num]+=1
    res = []
    for num in m:
        if num < 1 or num > 10:
            res.append(0)
        else:
            res.append(hash_list[num])
    return res
n = [5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
print(hashing(n,m))