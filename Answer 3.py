class cal():
    def __init__ (self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

    def mod(self):
        return self.a % self.b
a = int(input("Enter first element"))
b = int(input("Enter second element"))
obj = cal(a,b)

choice = 1
while choice !=0:
    print("0 Exit")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("5 Modlous")
    choice = int(input("Enter your choice"))
    if choice == 1:
        print("Result",obj.add())
    elif choice == 2:
        print("Result",obj.sub())
    elif choice == 3:
        print("Result",obj.mul())
    elif choice == 4:
        print("Result",obj.div())
    elif choice == 5:
        print("Result",obj.mod())
    elif choice == 0:
        print("Exiting")
    else:
        print("Invalid Choice")
    
        
