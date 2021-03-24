from account_types.main_account import Account
class SavingsAccount(Account):
    def withdraw(self,amount):
        if self.balance < 25:
            self.account_active == False
            print("Account is inactive; minimum balance required is $25.00 or more. ")
        else:
            super().withdraw(amount)
    def deposit(self, amount):
        if self.balance + amount <=25:
            super().deposit(amount)
            self.account_active == True
        else:
            super().deposit(amount)
            self.account_active == False

svgacct1=SavingsAccount(30,0.5)
print(str(svgacct1.balance_total())+" "+str(svgacct1.starting_balance))
print(str(svgacct1.account_active))
svgacct1.withdraw(15)
print(str(svgacct1.account_active))
svgacct1.withdraw(15)
print(str(svgacct1.account_active))
print(str(svgacct1.balance_total()))
print(str(svgacct1.deposit_total))