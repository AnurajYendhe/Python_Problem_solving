# Find the frequancy of the numbers in the list
def Frequancy(arr,No):
    counter = 0
    for i in arr:
        if(No == i):
            counter = counter + 1
    return counter

def main():
    arr = list()
    size = int(input("Enter the size of list : "))
    print("Enter the elements of list : ")
    for i in range(0,size,1):
        element = int(input())
        arr.append(element)

    No = int(input("Enter the Numbers that we want to frequancy : "))
    iRet = Frequancy(arr,No)
    print("Frequancy of {} in the list is {}".format(No,iRet))

if __name__ == "__main__":
    main()