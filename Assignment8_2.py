
i = 1
def Display(No):
    global i
    if(i <= No):
        print(i,end = "  ")
        i = i + 1
        Display(No)

def main():
    No = int(input("Enter the numbers : "))
    Display(No)

if __name__ == "__main__":
    main()