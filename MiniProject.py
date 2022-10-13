from optparse import Option


class Wallet:
    def __init__(self, balance):
        self.balance = 100


    def Login(self, code):
      self.Code = input("Code")

    def Deposit(self, Amount):
        self.balance = self.balance + Amount
        print(self.balance)
        

    def withdraw(self, Amount):
        self.balance = self.balance - Amount
        print(self.balance)

if __name__ == "__main__":
   # wallet_type = Wallet()

    # while True:
    #   print("1.Deposit")
    #   xyz= int(input())
    #   if xyz == 1:
    #     Amount = int(input("Enter deposit ammount:  "))
    #     wallet_type.Deposit(Amount)

    print("Welcome to the bank.")
while True:
    #Wallet = int(input("Which account number are you working with today? "))
 
    print("Would you like to:")
    print(" 1. Check the balance")
    print(" 2. Deposit money")
    print(" 3. Withdraw money")
    print(" 4. Quit")
    Option = input("Pick in option: ")
    if Option=="1":
        print("Balance: ")

    elif Option=="2":
        Amount=int(input("How much would you like to deposit? "))
        Wallet.Deposit(Amount)

    elif Option=="3":
        Amount=int(input("How much would you like to withdraw? "))
        if Wallet.withdraw(Amount) < 0:
            print("Unable to process. Doing this will result in a negative balance.")

    elif Option=="4":
        break

    else:
        print("Unrecognized.")



