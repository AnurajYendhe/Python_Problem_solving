# Check Numbers is Even or Odd
def ChkNum(No):
    if((No % 2) == 0):
        return True
    else:
        return False
    
def main():
    No = 0
    bRet = False
    
    No = int(input("Enter the Numbers : "))
    bRet = ChkNum(No)
    if(bRet == True):
        print("Even Number.")
    else:
        print("Odd Number.")

if __name__ == "__main__":
    main()