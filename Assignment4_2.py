# lambda Function for return Multiplication of two numbers

Multiplication = lambda X,Y : X * Y

def main():
    No1 = int(input("Enter the first Number : "))
    No2 = int(input("Enter the second Number : "))
    iRet = Multiplication(No1,No2)
    print("Multiplication of that numbers is : ",iRet)

if __name__ == "__main__":
    main()