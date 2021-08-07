class BankAccount:
    bank_name = "Greatest Bank Ever"
    all_accounts = []
    def __init__(self, interest, balance=0):
        self.interest = interest
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(amount > self.balance):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance*self.interest)
        return self

    @classmethod
    def show_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()



