from babel.numbers import format_currency
from Assignment2.account_types.main_account import Account
class SavingsAccount(Account):
    def account_active(self):
        if self.balance < 25:
            return super().set_account_inactive()
        else:
            return super().set_account_active()

    def withdraw(self,amount):
        self.account_active()
        if self.account_status == False:
            print("Account is inactive; minimum balance required is $25.00. ")
        elif (self.balance - amount) < 0:
            print("Cannot withdraw; Insufficient funds.")
        else:
            super().withdraw(amount)
            print(format_currency(amount, 'USD', locale='en_US') + " was successfully withdrawn.")

    def deposit(self, amount):
        if self.balance + amount >= 25:
            super().deposit(amount)
            super().set_account_active()
        else:
            super().deposit(amount)
        print(format_currency(amount, 'USD', locale='en_US') + " was successfully deposited.")

    def service_charges(self,amount):
        super().service_charges(amount)


