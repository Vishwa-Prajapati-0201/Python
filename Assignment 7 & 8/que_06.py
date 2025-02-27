# Create a class "BankAccount" with attributes account number and balance. Implement
# methods to deposit and withdraw funds, and a display method to show the account details.

class BankAccount:
    def __init__(self, account_number, balance=0.0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}. New Balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}. Remaining Balance: {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

if __name__ == "__main__":
    acc_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    account = BankAccount(acc_number, initial_balance)
    
    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Account")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 3:
            account.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice! Please try again.")