# Addition of digits
sum = 0
def AddDigits(No):
    global sum
    if(No != 0):
        sum = sum + (No % 10)
        No = No // 10 
        Display(No)

    return sum

def main():
    No = int(input("Enter the numbers : "))
    iRet = AddDigits(No)
    print("Summation of its digits is ",iRet)

if __name__ == "__main__":
    main()