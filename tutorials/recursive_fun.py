

# recursive function is a function that calls itself as part of its execution
def myfun(n):
    if n == 0:
        return 1
    else:
        return n + myfun(n-1)

test= myfun(3)
print(test)
