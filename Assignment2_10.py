# return Addition of digits in that numbers
def AdditionDigits(No):
    sum = 0
    while(No != 0):
        sum = sum + (No % 10)
        No = No // 10
    return sum

def main():
    No = 0
    iRet = 0
    No = int(input("Enter the Numbers : "))
    iRet = AdditionDigits(No)
    print("Addition of Digits in that Number is : ",iRet)

if __name__ == "__main__":
    main()