# Maximun number in the list 
def Maximun(arr):
    max = 0
    for i in arr:
        if(max < i):
            max = i 
    return max

def main():
    arr = list()
    size = int(input("Enter the size of list : "))
    print("Enter the elements of list : ")
    for i in range(0,size,1):
        element = int(input())
        arr.append(element)

    iRet = Maximun(arr)
    print("Maximun elements in the list is : ",iRet)

if __name__ == "__main__":
    main()