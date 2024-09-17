# Check Numbers is positive, Negative or Zero(0)
def ChkNum(No):
    if(No > 0):
        print("Positive Number.")
    elif(No < 0):
        print("Negative Number.")
    else:
        print("Number is zero(0)")
    
def main():
    No = 0
    No = int(input("Enter the Numbers : "))
    ChkNum(No)

if __name__ == "__main__":
    main()