def char_hash(s,q):
    li = [0]*26
    for c in s:
        ascii_value = ord(c)
        index = ascii_value-97
        li[index]+=1
    for c in q:
        ascii_value = ord(c)
        index = ascii_value-97
        print(li[index])
s = "azyxyyzaaaa"
q = ["d","a","y","x"]
print(char_hash(s,q))