# multi threading (create two thread first display 1 - 50 and second thread display 50 - 1)

import threading

def Task1():
    print("Printing 1 - 50 ...")
    for i in range(1,51,1):
        print(i)

def Task2():
    print("Printing 50 - 1...")
    for i in range(50,0,-1):
        print(i)

def main():
    
    thread1 = threading.Thread(target = Task1,args = ())
    thread2 = threading.Thread(target = Task2,args = ())

    thread1.start()
    thread1.join()

    thread2.start()
    thread2.join()

if __name__ == "__main__":
    main()