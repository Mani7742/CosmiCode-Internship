# Define a class for a bank account with attributes for account number, balance, and owner name. Include methods for deposit, withdrawal, and transfer.

class BankAccount:

    def __init__(self, account_number, owner_name, initial_balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def transfer(self,target_account,amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False
if __name__ == "__main__":
    account1 = BankAccount("123456", "Amna", 1000)
    account2 = BankAccount("654321", "Abdullah Bhai", 500)

    print("Initial Balances:")
    print(f"Account 1 ({account1.owner_name}): {account1.balance}")
    print(f"Account 2 ({account2.owner_name}): {account2.balance}")

    print("\nDepositing $200 into Account 1...")
    account1.deposit(200)
    print(f"Account 1 ({account1.owner_name}): {account1.balance}")

    print("\nWithdrawing $100 from Account 2...")
    account2.withdraw(100)
    print(f"Account 2 ({account2.owner_name}): {account2.balance}")

    print("\nTransferring $300 from Account 1 to Account 2...")
    account1.transfer(account2, 300)
    print(f"Account 1 ({account1.owner_name}): {account1.balance}")
    print(f"Account 2 ({account2.owner_name}): {account2.balance}")