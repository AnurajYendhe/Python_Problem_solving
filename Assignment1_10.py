# Length of string
def LengthX(Name):
    counter = 0
    for i in Name:
        counter = counter + 1

    return counter
    
def main():
    Name = None
    iRet = 0
    Name = input("Enter the Name : ")
    iRet = LengthX(Name)
    print("The length of string is : ",iRet)

if __name__ == "__main__":
    main()