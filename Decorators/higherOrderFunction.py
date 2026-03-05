# in Python function is a first class citizen
# we can pass function as a argument to another function
# we can return function from another function
# we can assign function to a variable

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def math_operation(func):
#     a=5
#     b=3
#     return func(a,b)

# print(math_operation(add))
# print(math_operation(sub))




def make_coffee():
    print("coffee is made")

def make_tea():
    print("tea is made")
def kitchen_robot(func):
    print("kitchen robot is starting...............")
    func()
    print("kitchen robot is stopped...............")


kitchen_robot(make_coffee)
kitchen_robot(make_tea)