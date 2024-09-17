# multi threading (create two thread first for display addition of all even elements of input list and second thread display addition of all odd elements of input list)

import threading

def Task1(arr):
    print("Calculating the addition of all even elements of the input list...")
    sum = 0
    for i in arr:
        if((i % 2 ) == 0 ):
            sum = sum + i 
    print("Addition of all even elements of the input list is : ",sum)

def Task2(arr):
    print("Calculating the addition of all odd elements of the input list...")
    sum = 0
    for i in arr:
        if((i % 2) != 0):
            sum = sum + i 
    print("Addition of all odd elements of the input list is : ",sum)

def main():
    size = int(input("Enter the size of list : "))

    arr = list()
    for i in range(0,size,1):
        elements = int(input())
        arr.append(elements)

    evenlist = threading.Thread(target = Task1,args = (arr,))
    oddlist = threading.Thread(target = Task2,args = (arr,))

    evenlist.start()
    oddlist.start()

    evenlist.join()
    oddlist.join()

if __name__ == "__main__":
    main()