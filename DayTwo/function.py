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


