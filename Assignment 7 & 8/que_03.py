# Write a Python program to create a class representing a bank. Include methods for managing
# customer accounts and transactions.

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = {"name": name, "balance": balance}
            print("Account created successfully.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]["balance"] += amount
            print("Deposit successful. New balance:", self.accounts[account_number]["balance"])
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number]["balance"] >= amount:
                self.accounts[account_number]["balance"] -= amount
                print("Withdrawal successful. New balance:", self.accounts[account_number]["balance"])
            else:
                print("Insufficient balance.")
        else:
            print("Account not found.")

    def display_account(self, account_number):
        if account_number in self.accounts:
            print("Account Number:", account_number)
            print("Name:", self.accounts[account_number]["name"])
            print("Balance:", self.accounts[account_number]["balance"])
        else:
            print("Account not found.")

if __name__ == "__main__":
    bank = Bank()
    while True:
        print("\nOptions:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            acc_num = input("Enter account number: ")
            name = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(acc_num, name, initial_balance)
        elif choice == 2:
            acc_num = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(acc_num, amount)
        elif choice == 3:
            acc_num = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(acc_num, amount)
        elif choice == 4:
            acc_num = input("Enter account number: ")
            bank.display_account(acc_num)
        elif choice == 5:
            break
        else:
            print("Invalid choice! Please try again.")