class Demo:
    value = 0 
    def __init__(self,i,j):
        self.no1 = i 
        self.no2 = j

    def fun(self):
        print("Value of no1 is : ",self.no1)

    def gun(self):
        print("Value of no2 is : ",self.no2)

def main():
    no1 = int(input("Enter the value for no1 : "))
    no2 = int(input("Enter the value for no2 : "))

    obj1 = Demo(no1,no2)

    no1 = int(input("Enter the value for no1 : "))
    no2 = int(input("Enter the value for no2 : "))

    obj2 = Demo(no1,no2)

    obj1.fun()
    obj2.fun()

    obj1.gun()
    obj2.gun()
    
if __name__ == "__main__":
    main()