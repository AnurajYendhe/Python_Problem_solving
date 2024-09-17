# return the numbers of digits in that numbers
def CountDigits(No):
    counter = 0
    while(No != 0):
        No = No // 10
        counter = counter + 1 

    return counter       
        
def main():
    No = 0
    iRet = 0
    No = int(input("Enter the Numbers : "))
    iRet = CountDigits(No)
    print("Total Numbers of Digits in that Number is : ",iRet)

if __name__ == "__main__":
    main()