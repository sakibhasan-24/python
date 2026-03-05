# decorator is a wrapper function that wraps another function and extends its functionality
# decorator is a function that takes a function as an argument and returns a function
# decorator returns a function that is wrapped around the original function
# decorator is a function that is used to modify the behavior of another function
# decorator is a function that is used to add functionality to another function

# decorator

def my_decorator(func):
    def wrapper(a,b):
        print("before function execution")
        result= func(a,b)
        print("after function execution")
        return result
    return wrapper

@my_decorator
def add(a,b):
    return a+b


print(add(1,2))