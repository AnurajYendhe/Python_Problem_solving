# lambda Function for return power of 2 to the input number

power = lambda x : 2 ** x

def main():
    No = int(input("Enter the Number to find the power of 2 : "))
    iRet = power(No)
    print("the power of two of that numbers is : ",iRet)

if __name__ == "__main__":
    main()