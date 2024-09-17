# * squre pattern
def Display(No):
    for i in range(No):
        for j in range(No):
            print("*",end = "   ")
        print('   ')
def main():
    No = 0
    
    No = int(input("Enter the Numbers : "))
    Display(No)

if __name__ == "__main__":
    main()