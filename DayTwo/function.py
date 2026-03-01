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