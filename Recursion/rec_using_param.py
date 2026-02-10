#Head recursion using parameters
def rec_param(x,n):
    if n == 0:
        return
    print(x)
    rec_param(x,n-1)
rec_param(15,3)

#Tail recursion usung parameters
def rec_param_tail(i,n):
    if i > n:
        return
    rec_param_tail(i+1,n)
    print(i)
rec_param_tail(0,3)