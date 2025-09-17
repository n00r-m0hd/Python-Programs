# Write a program to practice the concept of Class and Object in Python

class Smartphone:
    #constructor

    def __init__(self, device, name):
        self.device = device
        self.name =name


    # method of the class

    def description(self):
        return f"This is a {self.device} and its name is {self.name}"
    

# Object/ Instance of the class

phoneObj = Smartphone("Iphone","Iphone 16 ")

print(phoneObj.description())
    
