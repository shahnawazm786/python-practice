'''
Simple Banking System (Account, Deposit, Withdraw)
Create a basic banking system where: A user has an account
They can deposit or withdraw money
Withdrawal should fail if insufficient balance
'''
class Account:
    def __init__(self,account_name,balance):
        self.account_name=account_name
        self.balance=balance
    
    def Deposit(self,amount):
        self.balance+=amount
        print(f'{amount} is Deposited.')
        print(f'Your current balance is {self.balance}')

    def Withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f'{amount} is Withdraw.')
            print(f'Your current balance is {self.balance}')
        else:
            raise Exception('Insufficient balance')
    
a=Account("Shahnawaz",10000)
a.Deposit(50000)
a.Withdraw(65000)
    