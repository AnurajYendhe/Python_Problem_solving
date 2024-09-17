
class BankAccount:
    ROI = 10.5
    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount
        print("Welcome...",self.Name)
        print("Account is Successfully created with initial Balance is :",self.Amount)

        
    def Display(self):
        print("Hello...",self.Name)
        print("Your Balance is : ",self.Amount)

    def Deposit(self):
        Amount = int(input("Enter Deposite Amount : "))
        self.Amount = self.Amount + Amount
        print("Deposite Amount Successfully...")

    def Withdraw(self):
        Amount = int(input("Enter Withdraw Amount :"))
        if self.Amount< Amount :
            print("Their is No Sufficient Balance in Your Acount... ")
        else:
            self.Amount = self.Amount - Amount
            print("Amount withdraw succesfully...")  

    def CalculateIntrest(self):
        self.interst = 0
        self.interst = (self.Amount / 100) * BankAccount.ROI
        print("Your Interst is :",self.interst)             

def main():
    Name= str(input("Enter Account Holder Name :"))
    Amount = int(input("Enter Initial Amount : "))
    Obj1 = BankAccount(Name,Amount)
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Display()
    Obj1.Withdraw()
    Obj1.Display()
    Obj1.CalculateIntrest()

    Name= str(input("Enter Account Holder Name :"))
    Amount = int(input("Enter Initial Amount : "))
    Obj2 = BankAccount(Name,Amount)
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Display()
    Obj2.Withdraw()
    Obj2.Display()
    Obj2.CalculateIntrest()

if __name__ == "__main__":
    main()    