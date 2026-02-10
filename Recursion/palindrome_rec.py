def palindrome_rec(s, l, r):
    if l >= r:
        return True
    if s[l] != s[r]:
        return False
    return palindrome_rec(s, l+1, r-1)

s = "madam"
print(palindrome_rec(s, 0, len(s)-1))
