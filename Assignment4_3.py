# filter out such elements which is greater then or equal to 70 and less then or equal to 70 from the input list and map each elements increase by 10 and after that reduce is calculate the product of that elements

from functools import reduce

Less_Greater = lambda No : ((70 <= No) and (No <= 90))

Increase = lambda No : No + 10 

Product = lambda No1,No2 : No1 * No2


def main():
    arr = list()
    size = int(input("Enter the size of list : "))
    print("Enter the elements : ")
    for i in range(0,size,1):
        element = int(input())
        arr.append(element)

    print("The input list is : ",arr)

    filter_output = filter(Less_Greater,arr)
    print("List after filter is : ",filter_output)

    map_output = list(map(Increase,filter_output))
    print("List after map is : ",map_output)

    result = reduce(Product,map_output)
    print("Output after reduce is : ",result)
if __name__ == "__main__":
    main()