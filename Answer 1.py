class add():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

a = int(input("Enter Num1"))
b = int(input("Enter Num2"))

obj = add(a,b)
print("Addition of Num1 and Num2 is ", obj.add())
    
