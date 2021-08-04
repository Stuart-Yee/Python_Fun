from Python_OOP.User.User import User

user1 = User("Stuart", "stuart@stuart.com", 1000000)
user2 = User("Sal", "sal@codingdojo.com", 200000)
user3 = User("Amy Adams", "amy@amyadams.com", 5000000)

print(user1.name)
user1.make_deposit(50)
user1.make_deposit(100)
user1.make_deposit(200)
user1.make_withdrawal(100000)
user1.display_user_balance()

print(user2.name)
user2.make_deposit(5)
user2.make_deposit(10)
user2.make_withdrawal(100)
user2.make_withdrawal(20000)
user2.display_user_balance()

print(user3.name)
user3.make_deposit(1000000)
user3.make_withdrawal(500000)
user3.make_withdrawal(50000)
user3.make_withdrawal(800000)
user3.display_user_balance()

user1.transfer_money(user3, 100000)
