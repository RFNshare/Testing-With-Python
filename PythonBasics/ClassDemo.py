# Methods, class variables, instance variables, constructors
class Calculator:
    num = 100  # Class Variable

    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b
        a = 0  # Instance variable
        print("Constructor")

    def getData(self):
        print("Random Data From Class")

    def addition(self):
        return self.num1 + self.num2 + Calculator.num


# Class Variable are constant

obj = Calculator(2, 3)
result = obj.addition()
print(result)

obj1 = Calculator(4, 5)
result = obj1.addition()
print(result)
