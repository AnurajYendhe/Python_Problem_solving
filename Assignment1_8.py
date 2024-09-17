# print * of times input Number
def Display(No):
    for i in range(No):
        print("*",end = "   ")
    
def main():
    No = 0
    No = int(input("Enter the Numbers : "))
    Display(No)

if __name__ == "__main__":
    main()