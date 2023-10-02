"""Create Account class, with parameters currency and balance
Account class should have methods
* add_amount -  which  should return balance after amount add + currency
(balance -100, added_amount-10, currency -AMD -> Your method should return 110AMD)
* withdraw_amount - which  should return balance after withdrawal from the account + currency

Also you should have Saving Account class, which should have all the same parameters and methods,
and additionaly should have percentage parameter and method which will calculate final balance after percentage accumulation
(balance -100, percentage -10, -> Your method should return 110AMD)
"""


class Account:

    def __init__(self, currency, balance):
        self.balance = balance
        self.currency = currency

    def add_amount(self, amount):
        self.balance = self.balance + amount
        print(f'Account balance after adding {amount}:  {self.balance} {self.currency}')

    def withdraw_amount(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f'Account balance after withdrawing {amount}:  {self.balance} {self.currency}')
        else:
            print('Not enough funds')


class Savings(Account):
    def __init__(self, currency, balance, percentage):
        super().__init__(currency, balance)
        self.percentage = percentage

    def balance_with_percentage(self):
        self.balance = self.balance + (self.balance * self.percentage / 100)
        print(f'Saving balance after accumulation of percentage is {self.balance} {self.currency}')


account_amd = Account('AMD', 50000)
account_amd.add_amount(200)
account_amd.withdraw_amount(10)

saving_account = Savings("USD", 200, 10)
saving_account.add_amount(100)
saving_account.withdraw_amount(50)
saving_account.balance_with_percentage()


# Everythings is correct, only methods will be better return results, not print