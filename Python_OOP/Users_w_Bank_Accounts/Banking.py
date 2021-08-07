from Python_OOP.Users_w_Bank_Accounts.User import User

me = User("Stuart", "ki6fzb@gmail.com", 500)
me.display_user_balance()

she = User("Tabatha", amount=1000)

me.transfer_money(0,she,0,200)

me.open_account(300, .01)
me.display_user_balance(1)

me.transfer_money(0, me, 1, 100)

she.make_deposit(0, 100).open_account().make_deposit(1, 300).account_balances()