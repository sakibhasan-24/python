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



def security_check(func):
    def wrapper(user_key):
     
        if user_key == "1234": 
            print("✅ Access Granted! Guard is opening the door.")
            return func(user_key)
        else:
            print("❌ Access Denied! Wrong Key. Calling Police... 🚔")
    return wrapper


@security_check
def open_vault(key):
    print("💰 Welcome! You are now inside the vault. Take the money!")


print("--- Attempt 1: Wrong Key ---")
open_vault("wrong_pass")

print("\n--- Attempt 2: Correct Key ---")
open_vault("1234")