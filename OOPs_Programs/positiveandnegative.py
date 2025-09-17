class Positive:
    def __init__(self,num):

        self.num = num

    def check(self):

        if self.num == 0:

            print("Number is zero kinldy enter a valid number")

        elif self.num > 0:
            
            print("Number is positive")
        
        else:
            print("Number is negative")

obj = Positive(22)

obj.check()

obj1 = Positive(-11)

obj1.check()