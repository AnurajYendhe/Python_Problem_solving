# check numbers is prime or not
def CheckPrime(No):
    counter = 0
    for i in range(1,No,1):
        if((No % i) == 0):
            counter = counter + 1 

    if(counter > 1):
        return False
    
    else:
        return True
            
        
def main():
    No = 0
    bRet = False
    No = int(input("Enter the Numbers : "))
    bRet = CheckPrime(No)
    if(bRet == True):
        print("The numbers is Prime")

    else:
        print("The numbers is NOT Prime")

if __name__ == "__main__":
    main()