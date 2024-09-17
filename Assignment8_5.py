# Addition of digits
fact = 1
def Factorial(No):
    global fact
    if(No != 0):
        fact = fact * No
        No = No - 1
        Factorial(No)       
    return fact

def main():
    No = int(input("Enter the numbers : "))
    iRet = Factorial(No)
    print("Factorial of the numbers is ",iRet)

if __name__ == "__main__":
    main()