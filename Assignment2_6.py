
def Display(No):
    for i in range(0,No,1):
        for j in range(0,No,1):
            if(j >= i):
                print("*",end="")
            else:
                print("",end="")

        print()
            
        
def main():
    No = 0
    No = int(input("Enter the Numbers : "))
    Display(No)

if __name__ == "__main__":
    main()