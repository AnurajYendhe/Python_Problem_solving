# addition of all factors of a Numbers
def Factors(No):
    sumFact = 0
    for i in range(1,No,1):
        if((No % i) == 0):
            sumFact = sumFact + i 
            
    return sumFact
        
def main():
    No = 0
    iRet = 0
    No = int(input("Enter the Numbers : "))
    iRet = Factors(No)
    print("Addition of all factors of the numbers is : ",iRet)

if __name__ == "__main__":
    main()