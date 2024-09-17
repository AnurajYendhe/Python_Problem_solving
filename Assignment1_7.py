# Check Numbers Divisiable 5 or NOT
def Divisiable(No):
    if(No % 5) == 0:
        return True
    else:
        return False
    
def main():
    No = 0
    bRet = False
    No = int(input("Enter the Numbers : "))
    bRet = Divisiable(No)
    if(bRet == True):
        print("The Numbers is divisiable by 5")

    else:
        print("The Numbers is not divisiable by 5")
if __name__ == "__main__":
    main()