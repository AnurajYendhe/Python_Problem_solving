# print first 10 even numbers
def EvenNum(No):
    for i in range(1,No + 1,1):
        print(i * 2 ,end = "   ")
    
def main():
    EvenNum(10)

if __name__ == "__main__":
    main()