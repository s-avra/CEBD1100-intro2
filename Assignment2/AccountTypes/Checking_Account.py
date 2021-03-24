from Account import Account

class CheckingAccount(Account):
    def withdraw(self,amount):
        if self.balance - amount <0:
            print("Cannot withdraw")
            self.balance = self.balance-15
        else:
            super().withdraw(amount)
    def deposit(self, amount):
        super().deposit(amount)



checkingacct1 = CheckingAccount(10,.04)
print(str(checkingacct1.balance) + " " + str(checkingacct1.interest_rate))
checkingacct1.deposit(30)
print(checkingacct1.balance_total())
print(checkingacct1.deposit_count)
print(checkingacct1.starting_balance)
checkingacct1.deposit(60)
print(checkingacct1.balance_total())
print(checkingacct1.starting_balance)
checkingacct1.withdraw(80)
print(str(checkingacct1.balance_total())+"\n"+str(checkingacct1.deposit_count)+"\n"+str(checkingacct1.starting_balance) + "\n"+str(checkingacct1.withdraw_count))
print("\n")
print("Withdrawal amount "+str(checkingacct1.withdraw_total)+ " Deposit amount " +str(checkingacct1.deposit_total))

