# Factorial of a Numbers
def Factorial(No):
    fact = 1
    for i in range(1,No + 1,1):
        fact = fact * i

    return fact
        
def main():
    No = 0
    iRet = 0
    No = int(input("Enter the Numbers : "))
    iRet = Factorial(No)
    print("Factorial of the numbers is : ",iRet)

if __name__ == "__main__":
    main()