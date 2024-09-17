
def Display(No):
    for i in range(1,No + 1,1):
        for j in range(1,No + 1,1):
            print(j,end = "  ")

        print()
            
        
def main():
    No = 0
    No = int(input("Enter the Numbers : "))
    Display(No)

if __name__ == "__main__":
    main()