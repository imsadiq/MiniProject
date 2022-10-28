class Wallet:
    def __init__(self):
        self.balance = 100
    
    def Deposit(self, Amount):
        self.balance = self.balance + Amount
        print(self.balance)

    def withdraw(self, Amount):
        self.balance = self.balance - Amount
        print(self.balance)

class Dad(Wallet):
        def __init__(self, logincode, block):
              Wallet.__init__(self)
              self.logincode = logincode
              self.block = block
              
class Mom(Wallet):
        def __init__(self, logincode, viewrequest):
              Wallet.__init__(self)
              self.logincode = logincode
              self.viewrequest = viewrequest

class Kid(Wallet):
        def __init__(self, logincode, request):
              Wallet.__init__(self)
              self.logincode = logincode
              self.request = request

#Login Access Codes
dad_1 = Dad(110, "block")  

mom_1 = Mom(111, "see request")

Kid_1 = Kid(222, "request")

if __name__ == "__main__":
    wallet_type=Wallet()

    print("Welcome to the Family Bank Wallet")
while True:

    print("Enter Login Code: ")
    Login = int(input("Login Code: "))
    if Login == dad_1.logincode: 
       print("Welcome Dad, Your Access Options are below:")  
       print(" 1.Wallet Balance")
       print(" 2.Add Money To Wallet")
       print(" 3.Make Transaction")
       print(" 4.Block Member From Using Wallet")
       print(" 5.Logout")
       Option = input("Choose an option: ")
       if Option=="1":
            print("Balance: ", wallet_type.balance)

       elif Option=="2":
            Amount = int(input("How much amount would you like to deposit? "))
            wallet_type.Deposit(Amount)

       elif Option=="3":
            Amount = int(input("How much amount you want to transact "))
            if wallet_type.withdraw(Amount) < 0:
               print("Low Balance.")

       elif Option=="4":
            dad_1.block
            print("Member Blocked.")

       elif Option=="5":
            break

    elif Login == mom_1.logincode :   
       print("Welcome Mom, Your Access Options are below:")  
       print(" 1.Wallet Balance")
       print(" 2.Add Money To Wallet")
       print(" 3.Make Transaction")
       print(" 4.See Requests")
       print(" 5.Logout")
       Option = input("Pick an option: ")
       if Option=="1":
            print("Balance: ", wallet_type.balance)

       elif Option=="2":
            Amount = int(input("How much amount would you like to deposit? "))
            wallet_type.Deposit(Amount)

       elif Option=="3":
            Amount = int(input("How much amount you want to transact "))
            if wallet_type.withdraw(Amount) < 0:
               print("Low Balance.")

       elif Option=="4":
            print("Review Request.")
            mom_1.viewrequest

       elif Option=="5":
            break

    elif Login == Kid_1.logincode:   
       print("Welcome Kid, Your Access Options are below:")  
       print(" 1.Wallet Balance")
       print(" 2.Make Transaction")
       print(" 3.Make a Request")
       print(" 5.Logout")
       Option = input("Choose an option: ")
       if Option=="1":
            print("Balance: ", wallet_type.balance)

       elif Option=="2":
            Amount = int(input("How much amount you want to transact "))
            if wallet_type.withdraw(Amount) > 50:
               print("Not Allowed.")

       elif Option=="3":
            print("What Request you want to make? ") 
            print(" 1.Request Money Deposit ")
            print(" 2.Request Overpay")
            print(" 3.Request Second Transaction")
            Option = input("Choose an option: ")
            if Option=="1":
               Kid_1.request
               print("Send Money Deposit Request to Dad & Mom")

            elif Option=="2":
               Kid_1.request
               print("Send Overpay Request")
 
            elif Option=="3":
               Kid_1.request
               print("Send Second Transaction Request")

            else:
               print("Not Applicable")

       elif Option=="4":
            break

    else:
           print("Not a User")