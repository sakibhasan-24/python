# we will avoid global variables
# use main function




def show_balance(balance):
   
    print(f"\n[INFO] Current balance: ${balance:.2f}")

def deposit(balance):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("[ERROR] Amount must be greater than zero.")
            return balance
        
        new_balance = balance + amount
        print(f"[SUCCESS] ${amount:.2f} deposited.")
        return new_balance
    except ValueError:
        print("[ERROR] Invalid input. Please enter a number.")
        return balance

def withdraw(balance):
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("[ERROR] Amount must be positive.")
        elif amount > balance:
            print("[ERROR] Insufficient funds!")
        else:
            balance -= amount
            print(f"[SUCCESS] ${amount:.2f} withdrawn.")
        return balance
    except ValueError:
        print("[ERROR] Invalid input. Please enter a number.")
        return balance

def main():
    current_balance = 0.0
    is_running = True

    while is_running:
        print("\n" + "="*20)
        print("  PYTHON BANK ATM  ")
        print("="*20)
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")

        if choice == '1':
            show_balance(current_balance)
        elif choice == '2':
            current_balance = deposit(current_balance)
        elif choice == '3':
            current_balance = withdraw(current_balance)
        elif choice == '4':
            is_running = False
        else:
            print("[ERROR] Invalid choice, try again.")

    print("\nThank you for using our service. Goodbye!")

if __name__ == "__main__":
    main()