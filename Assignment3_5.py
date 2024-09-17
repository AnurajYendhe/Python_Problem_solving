# Find the frequancy of the numbers in the list
from functools import reduce
import MarvellousNum

def ListPrime(A,B):
    ans = 0
    ans = A + B
    return ans

def main():
    arr = list()
    size = int(input("Enter the size of list : "))
    print("Enter the elements of list : ")
    for i in range(0,size,1):
        element = int(input())
        arr.append(element)

    output = list(filter(MarvellousNum.CheckPrime,arr))
    result = reduce(ListPrime,output)
    print("Addition of all prime numbers is : ",result)

if __name__ == "__main__":
    main()