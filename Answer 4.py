class printastring():
    def __init__(self):
        self.string = ""

    def get(self):
        self.string = input("Enter the string")

    def put(self):
        print("the printed strig is",self.string)

obj = printastring()
obj.get()
obj.put()
