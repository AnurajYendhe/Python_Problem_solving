# addition of all numbers in the list 
def Addition(arr):
    sum = 0
    for i in arr:
        sum = sum + i 
    return sum
    
def main():
    arr = list()
    size = int(input("Enter the size of list : "))
    print("Enter the elements of list : ")
    for i in range(0,size,1):
        element = int(input())
        arr.append(element)

    iRet = Addition(arr)
    print("Addition of all the elements in the list is : ",iRet)

if __name__ == "__main__":
    main()