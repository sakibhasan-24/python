
balance=0
is_processing=True

while is_processing:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice =(input("Enter your choice: "))

    if choice == "1":
        print("deposit")
    elif choice == "2":
        print("withdraw")
    elif choice == "3":
        print(f"Your balance is ${balance:.2f}")
    elif choice == "4":
        is_processing = False
    else:
        print("Invalid choice")

print("Thank you for banking with us")