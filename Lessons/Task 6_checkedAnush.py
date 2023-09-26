# """Create Account class, with parameters currency and balance
# Account class should have methods
# * add_amount -  which  should return balance after amount add + currency
# (balance -100, added_amount-10, currency -AMD -> Your method should return 110AMD)
# * withdraw_amount - which  should return balance after withdrawal from the account + currency

class Account:

    def __init__(self, balance, currency: str = 'AMD'):
        self.balance = balance
        self.currency = currency

    def withdraw(self):
        amount = float(input("add widthraw amount: "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print(f"{self.balance}{self.currency}")
        else:
            print("Insuficient Balance")

    def add_amount(self):
        amount = int(input("add amount: "))
        self.balance = self.balance + amount
        print(f"{self.balance}{self.currency}")



x = Account(100, ' AMD')
print(x.add_amount())
print(x.withdraw())
# class Account:
#
#     def __init__(self, balance, currency: str='AMD'):
#         self.balance = balance
#         self.currency = currency
#
#     def __add__(self, amount):
#         return Account(self.balance + amount.balance)
#
#
# obj1 = Account(10, 'AMD')
# obj2 = Account(1200, 'AMD')
# obj3 = obj1 + obj2
# print(f"{obj3.balance} AMD")



# Also you should have Saving Account class, which should have all the same parameters and methods,
# and additionaly should have percentage parameter and method which will calculate final balance after percentage accumulation
# (balance -100, percentage -10, -> Your method should return 110

class Saving_Account:

    def __init__(self, balance, currency: str = 'AMD'):
        self.balance = balance
        self.currency = currency

    def add_persentage(self):
        pers = float(input("add persentage: "))
        self.balance = self.balance + (self.balance * pers/100)
        print(f"{self.balance}{self.currency}")

y = Saving_Account(200, ' AMD')
print(y.add_persentage())

# Anna comment - All methods should return value, not print
# Saving account class should be inherited from Account class and get percentage as argument in init method