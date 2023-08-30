

#closure function is a nested function return inner function

def outerfun():
    def innerfun():
        print("Hello word")
    return innerfun


closure_instance = outerfun()

print(closure_instance)
