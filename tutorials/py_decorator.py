def my_decorator(fun):
    def innerfun():
        print('Before the function call')
        fun()
        print("After the function call")
    return innerfun()

# we can use decoractor function assign to variable or using @

def argfun():
    print("Hello World")

ans = my_decorator(argfun)
print(ans)

@my_decorator
def hello():
    print("hello world")
