# Minimun number in the list 
def Minimun(arr):
    min = arr[0]
    for i in arr:
        if(min > i):
            min = i 
    return min

def main():
    arr = list()
    size = int(input("Enter the size of list : "))
    print("Enter the elements of list : ")
    for i in range(0,size,1):
        element = int(input())
        arr.append(element)

    iRet = Minimun(arr)
    print("Minimun elements in the list is : ",iRet)

if __name__ == "__main__":
    main()