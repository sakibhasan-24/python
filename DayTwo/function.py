def make_coffee():
    print("Making coffee")


print("starting")
make_coffee()
print("ending")


# def clean_text():
#     name=" SakiB  "
#     print(name.strip().lower())


# clean_text()


def clean_text(name):
    print(name.strip().lower().capitalize())


clean_text(" sakiB  ")
clean_text("  SakiB  ")
clean_text("  BangladeSh  ")




# argument vs parameter 

# argument is input pass when function call
# parameter is input pass when function define


def create_emoji(eyes, mouth):
    # here eyes and mouth is parameter
    print(f" {eyes} {mouth} {eyes} ")


create_emoji("O", "D")
# here O and D is argument
create_emoji("X", "X")
# here X and X is argument


# return statement


def create_random_emoji(emoji):
    if emoji =="":
        return "😀"
    else:
        return emoji
    
print(create_random_emoji("😂"))


# default argument

def  power(num, power=2):
    return num**power

print(power(2,3))
print(power(2))



# args vs kwargs
# args means arguments 

# *args allows function to accept unlimited positional arguments

def sum_all(*args):
    # print(*args)
    for c in args:
        if type(c) is not int:
            print("Please enter only integer")
            return
    total=0
    for num in args:
        total+=num
    print(total)
sum_all(1,2,3,4,5,6,7)



# *kwargs allows function to accept unlimited keyword arguments

def create_user(**kwargs):
    print(kwargs)
    print(kwargs["name"])
    print(kwargs["age"])

create_user(name="John", age=25)
create_user(name="Jane", age=30, city="New York", country="USA", email="jane@gmail.com")




# scope
# it means where variable can be accessed or alive


count =0

print(f"initial value of count {count}")
def increment():
    global count
    count=count+1
    # so we make this count global or call function to access it 
    print(f"inside function {count}")


print(f"outside function {count} before call function")
increment()
print(f"outside function {count} after call function")