from account_types.main_account import Account
class CheckingAccount(Account):
    def withdraw(self,amount):
        if self.balance - amount <0:
            print("Cannot withdraw")
            self.balance = self.balance-15
        else:
            super().withdraw(amount)
    def deposit(self, amount):
        super().deposit(amount)
chkgacct1 = CheckingAccount(10,.04)
print(str(chkgacct1.balance) + " " + str(chkgacct1.interest_rate))
chkgacct1.deposit(30)
print(chkgacct1.balance_total())