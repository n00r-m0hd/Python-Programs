# class Add:
#     def __init__(self,a ,b):

#         self.a = a
#         self.b = b

#     def show(self):
#         return self.a + self.b
    
# obj = Add(22,33)

# print(obj.show())    

# class Add:

#     def add(self):
#         self.a = int(input("Enter first number\n"))
#         self.b = int(input("Enter second number\n"))

#         self.sum = self.a + self.b

#         print(f"Sum is {self.sum}")

# obj1 = Add()
# obj1.add()

class Add:

    def show(self, a, b):

        self.a = a
        self.b = b

        print(self.a + self.b)

obj = Add()

obj.show(11,22)