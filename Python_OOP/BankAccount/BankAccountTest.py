from Python_OOP.BankAccount.BankAccount import BankAccount

Account1 = BankAccount(.12)
Account2 = BankAccount(.15, 3000)

Account1.deposit(5).deposit(5).deposit(8).withdraw(300).yield_interest().display_account_info()

Account2.deposit(2).deposit(2).withdraw(3000).withdraw(5).withdraw(1).withdraw(400).yield_interest().display_account_info()

BankAccount.show_all_accounts()