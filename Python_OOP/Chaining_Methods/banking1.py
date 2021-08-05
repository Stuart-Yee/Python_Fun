from Python_OOP.Chaining_Methods.User import User

user1 = User("Stuart", "stuart@stuart.com", 1000000)
user2 = User("Sal", "sal@codingdojo.com", 200000)
user3 = User("Amy Adams", "amy@amyadams.com", 5000000)

print(user1.name)
user1.make_deposit(50).make_deposit(100).make_deposit(200).make_withdrawal(100000).display_user_balance()

print(user2.name)
user2.make_deposit(5).make_deposit(10).make_withdrawal(100).make_withdrawal(20000).display_user_balance()

print(user3.name)
user3.make_deposit(1000000).make_withdrawal(500000).make_withdrawal(50000).make_withdrawal(800000).display_user_balance()

user1.transfer_money(user3, 100000)
