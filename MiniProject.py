from tkinter import W


class Wallet:
    # def __init__(self, balance):
    #     self.balance = 100
    #     print(self.balance)
    def __init__(self):
        self.balance = 0
        print(self.balance)

    def Login(self, code):
      self.Code = input("Code")
    
    def Deposit(self, Amount):
        self.balance = self.balance + Amount
        print(self.balance)

    def withdraw(self, Amount):
        self.balance = self.balance - Amount
        print(self.balance)

class Dad(Wallet):
        def __init__(self, transaction):
              Wallet.__init__(self)
              self.transaction = transaction
        
class Mom(Wallet):
        def __init__(self, transaction, rewreq):
              Wallet.__init__(self)
              self.transaction = transaction
              self.rewreq = rewreq
class Kid(Wallet):
        def __init__(self, req):
            Wallet.__init__(self)
            self.req = req


if __name__ == "__main__":
    wallet_type=Wallet()

    # while True:
    #   print("1.Deposit")
    #   xyz= int(input())
    #   if xyz == 1:
    #     Amount = int(input("Enter deposit ammount:  "))
    #     wallet_type.Deposit(Amount)

    print("Welcome to the Family Bank Wallet")
    #User = Wallet()
while True:
    #Wallet = int(input("Which account number are you working with today? "))
 
    print("Would you like to:")
    print(" 1.Check the balance")
    print(" 2.Deposit money")
    print(" 3.Withdraw money")
    print(" 4.Quit")
    Option = input("Pick in option: ")
    if Option=="1":
        wallet_type.balance
        print("Balance: ")
        #wallet_type.balance()

    elif Option=="2":
        Amount = int(input("How much would you like to deposit? "))
        wallet_type.Deposit(Amount)

    elif Option=="3":
        Amount = int(input("How much would you like to withdraw? "))
        if wallet_type.withdraw(Amount) < 0:
            print("Unable to process. Doing this will result in a negative balance.")

    elif Option=="4":
        break

    else:
        print("Unrecognized.")



