# multi threading (create three thread first for count the small characters of input string, second thread for count the capital characters of input string and thrid thread for count the digits of input string)

import threading

def Task1(string):
    count = 0
    for i in string:
        if(i.islower()):
            count = count + 1 

    print("Total numbers of small characters in that string is : ",count)
    print("Id of Task1 thread is : ",threading.get_ident())
    print("Name of Task1 thread is : ",threading.current_thread().name)
    
def Task2(string):
    count = 0
    for i in string:
        if(i.isupper()):
            count = count + 1 

    print("Total numbers of capital characters in that string is : ",count)
    print("Id of Task2 thread is : ",threading.get_ident())
    print("Name of Task2 thread is : ",threading.current_thread().name)
    
def Task3(string):
    count = 0
    for i in string:
        if(i.isdigit()):
            count = count + 1 

    print("Total numbers of digits in that string is : ",count)
    print("Id of Task3 thread is : ",threading.get_ident())
    print("Name of Task3 thread is : ",threading.current_thread().name)
       
def main():
    
    string = input("Enter the string : ")

    small = threading.Thread(target = Task1,args = (string,))
    capital = threading.Thread(target = Task2,args = (string,))
    digits = threading.Thread(target = Task3,args = (string,))

    small.start()
    capital.start()
    digits.start()

    small.join()
    capital.join()
    digits.join()

if __name__ == "__main__":
    main()