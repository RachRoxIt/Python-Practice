class BankAccount:

    def __init__ (self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    def withdrawal(self, amount):
       # if amount < 0:
        #    raise ValueError("Withdrawn amount is negative.")
        #if amount > self.balance:
         #   raise ValueError('Dont have sufficient funds')
     #   self.balance -= amount
        print("this is a {self.balance} test." )

cust_acct = BankAccount(123, 200) #im taking accounNumbr and balance from init
#cust_acct.withdrawal()
print(f"My account number is {cust_acct.accountNumber}.")
cust_acct.withdrawal()
#print(f"My balance is {cust_acct.balance}.")