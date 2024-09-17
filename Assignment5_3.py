
class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the First number : "))
        self.Value2 = int(input("Enter the Second number : "))

    def Addition(self):
        self.ans = self.Value1 + self.Value2
        return self.ans
        
    def Subtraction(self):
        self.ans = self.Value1 - self.Value2
        return self.ans
        
    def Multiplication(self):
        self.ans = self.Value1 * self.Value2
        return self.ans
        
    def Division(self):
        self.ans = self.Value1 / self.Value2
        return self.ans
        
def main():
    print("Performing opertation on obj1.")
    obj1 = Arithmetic()
    obj1.Accept()
    iRet = obj1.Addition()
    print("Addition is : ",iRet)
    iRet = obj1.Subtraction()
    print("Subtraction is : ",iRet)
    iRet = obj1.Multiplication()
    print("Multiplication is : ",iRet)
    iRet = obj1.Division()
    print("Division is : ",iRet)

    print("Performing opertation on obj2.")
    obj2 = Arithmetic()
    obj2.Accept()
    iRet = obj2.Addition()
    print("Addition is : ",iRet)
    iRet = obj2.Subtraction()
    print("Subtraction is : ",iRet)
    iRet = obj2.Multiplication()
    print("Multiplication is : ",iRet)
    iRet = obj2.Division()
    print("Division is : ",iRet)

    print("Performing opertation on obj3.")
    obj3 = Arithmetic()
    obj3.Accept()
    iRet = obj3.Addition()
    print("Addition is : ",iRet)
    iRet = obj3.Subtraction()
    print("Subtraction is : ",iRet)
    iRet = obj3.Multiplication()
    print("Multiplication is : ",iRet)
    iRet = obj3.Division()
    print("Division is : ",iRet)

    print("Performing opertation on obj4.")
    obj4 = Arithmetic()
    obj4.Accept()
    iRet = obj4.Addition()
    print("Addition is : ",iRet)
    iRet = obj4.Subtraction()
    print("Subtraction is : ",iRet)
    iRet = obj4.Multiplication()
    print("Multiplication is : ",iRet)
    iRet = obj4.Division()
    print("Division is : ",iRet)

    
if __name__ == "__main__":
    main()