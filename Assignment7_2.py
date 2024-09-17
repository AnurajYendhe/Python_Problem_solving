# multi threading (create two thread first for display addition of all even factors of input number and second thread display addition of all odd factors of input number)

import threading

def Task1(No):
    print("Calculating the addition of all even factor of that numbers...")
    sum = 0
    for i in range(1,No,1):
        if((No % i ) == 0 ):
            if((i % 2) == 0):
                sum = sum + i 
    print("Addition of all even factors of that numbers is : ",sum)

def Task2(No):
    print("Calculating the addition of all odd factor of that numbers...")
    sum = 0
    for i in range(1,No,1):
        if((No % i) == 0):
            if((i % 2) != 0):
                sum = sum + i 
    print("Addition of all odd factors of that numbers is : ",sum)

def main():
    No = int(input("Enter the numbers : "))

    evenfactor = threading.Thread(target = Task1,args = (No,))
    oddfactor = threading.Thread(target = Task2,args = (No,))

    evenfactor.start()
    oddfactor.start()

    evenfactor.join()
    oddfactor.join()

    print("exit from main")
if __name__ == "__main__":
    main()