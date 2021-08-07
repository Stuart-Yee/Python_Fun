from Python_OOP.Users_w_Bank_Accounts.BankAccount import BankAccount

class User:

    bank_name="Dojo Credit Union"

    def __init__(self, name=None, email=None, amount=None):
        self.name = name
        self.email = email
        self.accounts = [BankAccount(.02, amount)]

    def make_deposit(self, account=0, amount=None):
        print(f"Your current balance is ${self.accounts[account].balance}")
        print(f"You are depositing ${amount} today")
        self.accounts[account].deposit(amount)
        print(f"Your new balance is ${self.accounts[account].balance}")
        return self

    def make_withdrawal(self,account = 0, amount=None):
        if amount > self.accounts[account].balance:
            print(f"We're sorry! You're trying to withdraw ${amount} but you only have a balance of "
                  f"${self.accounts[account].balance}.")
            return self
        else:
            print(f"Your current balance is ${self.accounts[account].balance}")
            print(f"You're withdrawing ${amount} today.")
            self.accounts[account].withdraw(amount)
            print(f"Your new balance is ${self.accounts[account].balance}")
            return self

    def display_user_balance(self, account=0):
        self.accounts[account].display_account_info()
        return self

    def transfer_money(self, account=0, recipient=None, recAcct=0, amount=None):
        if amount > self.accounts[account].balance:
            print(f"We're sorry, there are insufficent funds to process. \nYou are trying to transfer ${amount}"
                  f"but you only have ${self.accounts[account].balance} available.")
            return self
        else:
            print(f"Transfering ${amount} from {self.name}'s account to {recipient.name}'s account.")
            print(f"Starting balances: \n{self.name}: ${self.accounts[account].balance} \n{recipient.name}: "
                  f"${recipient.accounts[recAcct].balance}")
            self.accounts[account].withdraw(amount)
            recipient.accounts[recAcct].deposit(amount)
            print(f"New balances: \n{self.name}: ${self.accounts[account].balance} \n{recipient.name}: "
                  f"${recipient.accounts[recAcct].balance}")
            return self

    def open_account(self, amount=0, interest=.05):
        self.accounts.append(BankAccount(interest,amount))
        return self

    def account_balances(self):
        for account in self.accounts:
            account.display_account_info()
        return self



