
balance=0
is_processing=True
def show_balance():
      print(f"Your balance is ${balance:.2f}")

def deposit():
    global balance
    amount=float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Your balance is now ${balance:.2f}")
        return amount
    else:
        print("Invalid amount")

def withdraw():
    global balance
    if balance< 0:
        print("Insufficient balance")
        return
    else:
        amount=float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance")
            return
        else:
            balance -= amount
            print(f"Your balance is now ${balance:.2f}")
            return amount
while is_processing:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice =(input("Enter your choice: "))

    if choice == "1":
        
        deposit()
    elif choice == "2":
       withdraw()
    elif choice == "3":
        show_balance()    
    elif choice == "4":
        is_processing = False
    else:
        print("Invalid choice")

print("Thank you for banking with us")