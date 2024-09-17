# multi threading (create two thread first for display even from 1 - 20 and second thread display odd numbers from 1 - 20 )

import threading

def Task1(No):
    print(f"First {No} Even Numbers is : ")
    for i in range(1,No,1):
        print(2 * i)

def Task2(No):
    print(f"First {No} Odd Numbers is : ")
    for i in range(1,No,1):
        print((2 * i) - 1)

def main():
    No = 11

    Even = threading.Thread(target = Task1,args = (No,))
    Odd = threading.Thread(target = Task2,args = (No,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()