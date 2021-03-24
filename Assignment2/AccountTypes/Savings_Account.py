from Account import Account
class SavingsAccount(Account):
    def withdraw(self,amount):
        if self.balance < 25:
            self.account_active == False
            print("Account is inactive; please deposit $25.00 or more to activate. ")
        else:
            super().withdraw(amount)
    def deposit(self, amount):
        if self.balance + amount <=25:
            super().deposit(amount)
            self.account_active == True
        else:
            super().deposit(amount)
            self.account_active == False