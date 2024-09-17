
class Numbers:

    def __init__(self,No):
        self.Value = No
        
    def ChkPrime(self):
        self.counter = 0
        for i in range(1,self.Value + 1,1):
            if(self.Value % i) == 0:
                self.counter = self.counter + 1
        if(self.counter == 2):
            return True
        else:
            return False

    def ChkPerfect(self):
        self.sum = 0
        for i in range(1,self.Value,1):
            if(self.Value % i) == 0:
                self.sum = self.sum + i
        if(self.sum == self.Value):
            return True
        else:
            return False  

    def Factors(self):
        for i in range(1,self.Value,1):
            if(self.Value % i) == 0:
                print(i)

    def SumFactors(self):
        self.sum = 0
        for i in range(1,self.Value,1):
            if(self.Value % i) == 0:
                self.sum = self.sum + i
        return self.sum
def main():
    
    Number = int(input("Enter the Numbers : "))
    Obj1 = Numbers(Number)
    bRet = Obj1.ChkPrime()
    if(bRet == True):
        print("Numbers is Prime.")
    else:
        print("Numbers is NOT Prime.")

    bRet = Obj1.ChkPerfect()
    if(bRet == True):
        print("Numbers is Perfect.")
    else:
        print("Numbers is NOT Perfect.")

    Obj1.Factors()

    iRet = Obj1.SumFactors()
    print("Addition of all factors is : ",iRet)

if __name__ == "__main__":
    main()    