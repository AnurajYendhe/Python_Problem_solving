# filter out such elements which is even from the input list and map calculate squre of each elements and after that reduce is calculate the addition of that elements

from functools import reduce

Even = lambda No : No % 2 == 0

Squre = lambda No : No * No 

Addition = lambda No1,No2 : No1 + No2


def main():
    arr = list()
    size = int(input("Enter the size of list : "))
    print("Enter the elements : ")
    for i in range(0,size,1):
        element = int(input())
        arr.append(element)

    print("The input list is : ",arr)

    filter_output = filter(Even,arr)
    print("List after filter is : ",filter_output)

    map_output = list(map(Squre,filter_output))
    print("List after map is : ",map_output)

    result = reduce(Addition,map_output)
    print("Output after reduce is : ",result)
if __name__ == "__main__":
    main()