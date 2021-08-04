class User:

    bank_name="Dojo Credit Union"

    def __init__(self, name=None, email=None, balance=None):
        self.name = name
        self.email = email
        self.balance = balance

    def make_deposit(self, amount=None):
        print(f"Your current balance is ${self.balance}")
        print(f"You are depositing ${amount} today")
        self.balance += amount
        print(f"Your new balance is ${self.balance}")

    def make_withdrawal(self, amount=None):
        if amount > self.balance:
            print(f"We're sorry! You're trying to withdraw ${amount} but you only have a balance of ${self.balance}.")
        else:
            print(f"Your current balance is ${self.balance}")
            print(f"You're withdrawing ${amount} today.")
            self.balance -= amount
            print(f"Your new balance is ${self.balance}")

    def display_user_balance(self):
        print(f"Your current balance is ${self.balance}")

    def transfer_money(self, recipient=None, amount=None):
        if amount > self.balance:
            print(f"We're sorry, there are insufficent funds to process. \nYou are trying to transfer ${amount}"
                  f"but you only have ${self.balance} available.")
        else:
            print(f"Transfering ${amount} from {self.name}'s account to {recipient.name}'s account.")
            print(f"Starting balances: \n{self.name}: ${self.balance} \n{recipient.name}: ${recipient.balance}")
            self.balance -= amount
            recipient.balance += amount
            print(f"New balances: \n{self.name}: ${self.balance} \n{recipient.name}: ${recipient.balance}")


