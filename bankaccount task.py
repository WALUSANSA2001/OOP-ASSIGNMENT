class BankAccount:
    interest_rate = 0.05  

    def __init__(self, account_holder,):
        self.account_holder = account_holder  
        self.balance = 0 
# method for depositing.
    def deposit(self, amount):
        self.balance += amount
#method for withdrawing.
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")
# method for supplimenting the intrest as of bank rules.
    def apply_interest(self):
        self.balance += self.balance * BankAccount.interest_rate
# method to display the account information if needed.
    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")

# Test the BankAccount class
Account1 = BankAccount("vicky")
Account2 = BankAccount("micheal")

# Perform operations
Account1.deposit(30000000)
Account1.withdraw(500000)
Account1.apply_interest()
Account1.display_account_info()

Account2.deposit(500000)
Account2.apply_interest()
Account2.display_account_info()
