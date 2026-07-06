class bank_account():
    def __init__(self,Account_number,Account_holder,Balance):
        self.Account_number=Account_number
        self.Account_holder=Account_holder
        self.Balance=Balance
    def display(self):
        print("the account number is", self.Account_number)
        print("the account holder is",self.Account_holder)
        print("the balance in the account is",self.Balance)
        
obj1=bank_account(23456789,"prithvi",250)
obj1.display()
        
class InvalidamountException(Exception):
    pass
 

while True:
    try:
        Deposite_amount=float(input("enter the amount you want to deposite:" ))
        if Deposite_amount<0:
            raise InvalidamountException
        else:
            print("you deposited your amount in your bank")
            break
    except InvalidamountException:
        print("❌ Error: Amount cannot be negative. Please try again.")
    
class InsufficientfundException(Exception):
    pass


balance=float(input("enter the amount of your balance:"))
while True:
    try:
        Withdraw_amount=float(input("enter the amount you want to withdraw:"))
        if Withdraw_amount>balance:
            raise InsufficientfundException
        else:
            print("withdrawal of your amount done")
            break
    except InsufficientfundException:
        print("amount is not sufficient for withdrawal")
        
x=Withdraw_amount+balance+Deposite_amount
print("the total balance in your account is",x)
