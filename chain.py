class User:
    def __init__ (self,name):
        self.name = name
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        if amount > self.account_balance:
            print ("insufficient funds")
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print (self.account_balance)
        return self

John = User("John Smith")
Andrew = User("Andrew Jones")
Jane = User("Jane Curtan")

John.make_deposit(200).make_deposit(100).make_deposit(50).make_withdrawal(300).display_user_balance()
Andrew.make_deposit(25).make_deposit(100).make_withdrawal(20).make_withdrawal(10).display_user_balance()
Jane.make_deposit(500).make_withdrawal(100).make_withdrawal(345).make_withdrawal(100).display_user_balance()