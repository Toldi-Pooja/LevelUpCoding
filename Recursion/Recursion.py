#head recursion - do job first and then function call
def func(count):
    if count >= 4:
        return
    print("Pooz")
    func(count + 1)

func(0)


#Tail recursion - call func first and then do job
def func1(count):
    if count >= 4:
        return
    func1(count + 1)
    print("Hii")

func1(0)
