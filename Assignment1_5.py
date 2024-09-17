# Demonstration of for loop in reverse oder
def Display(No):
    for i in range(No,0,-1):
        print(i,end = "   ")
    
def main():
    Display(10)

if __name__ == "__main__":
    main()