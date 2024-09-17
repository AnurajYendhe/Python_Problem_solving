# to perform the Addition, Subtraction, Multiplaction and Division
import Arithmetic

def main():
    No1 = 0
    No2 = 0
    iRet = 0
    
    No1 = int(input("Enter the first Numbers : "))
    No2 = int(input("Enter the second Numbers : "))

    iRet = Arithmetic.Add(No1,No2)
    print("Addition of this two numbers is : ",iRet)

    iRet = Arithmetic.Sub(No1,No2)
    print("Subtraction of this two numbers is : ",iRet)

    iRet = Arithmetic.Mult(No1,No2)
    print("Multiplaction of this two numbers is : ",iRet)

    iRet = Arithmetic.Div(No1,No2)
    print("Division of this two numbers is : ",iRet)

if __name__ == "__main__":
    main()