class rectangle():
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

a = int(input("Enter the length of rectangle"))
b = int(input("Enter the breadth of rectangle"))

obj = rectangle(a,b)
print("Area of rectangle is ", obj.area())
    
