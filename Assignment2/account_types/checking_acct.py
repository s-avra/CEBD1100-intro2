from babel.numbers import format_currency
from Assignment2.account_types.main_account import Account
class CheckingAccount(Account):
    def withdraw(self,amount):
        if self.balance - amount <0:
            print("Cannot withdraw, insufficient funds")
            self.balance = self.balance-15
        else:
            super().withdraw(amount)
            print(format_currency(amount, 'USD', locale='en_US') + " was successfully withdrawn")
    def deposit(self, amount):
        super().deposit(amount)
        print(format_currency(amount, 'USD', locale='en_US') + " was successfully deposited")
    def service_charges(self,amount):
        super().service_charges(amount)



chkgacct1 = CheckingAccount(10,.04)
print(str(chkgacct1.balance) + " " + str(chkgacct1.interest_rate))
chkgacct1.deposit(30)
print(chkgacct1.balance_total())
chkgacct1.doMonthlyReport()
chkgacct1.deposit(600)
chkgacct1.withdraw(5)
chkgacct1.withdraw(5)
chkgacct1.withdraw(5)
chkgacct1.withdraw(5)
chkgacct1.withdraw(5)
chkgacct1.withdraw(5)
chkgacct1.service_charges()

chkgacct1.service_charge(5)
chkgacct1.doMonthlyReport()