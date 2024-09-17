# filter out such elements which is Prime from the input list and map will be multiple each elements by ten and after that reduce is find maximun of that elements

from functools import reduce

def Prime(No):
    count = 0
    for i in range(1,No + 1,1):
        if(No % i ) == 0:
            count = count + 1

    if(count == 2):
        return True
    else:
        return False

multiple = lambda No : No * 2

def maximun(No1,No2):
    if(No1 < No2):
        return No2

def main():
    arr = list()
    size = int(input("Enter the size of list : "))

    print("Enter the elements : ")
    for i in range(0,size,1):
        element = int(input())
        arr.append(element)

    print("Input list is : ",arr)

    filter_output = list(filter(Prime,arr))
    print("List after filter is : ",filter_output)

    map_output = list(map(multiple,filter_output))
    print("List after Map is : ",map_output)

    result = reduce(maximun,map_output)
    print("result after reduce is : ",result)

if __name__ == "__main__":
    main()