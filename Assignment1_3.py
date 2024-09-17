# Addition of two numbers
def Add(i,j):
    ans = 0
    ans = i + j
    return ans
    
def main():
    No1 = 0
    No2 = 0
    iRet = 0
    
    No1 = int(input("Enter the first Numbers : "))
    No2 = int(input("Enter the second Numbers : "))
    iRet = Add(No1,No2)
    print("Addition of this two numbers is : ",iRet)

if __name__ == "__main__":
    main()