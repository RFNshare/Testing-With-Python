from PythonBasics import ClassDemo
from PythonBasics.ClassDemo import Calculator

# qwe = ClassDemo.Calculator(1, 3)
# res = qwe.addition()
# print(res)


class ChildCalculator(Calculator):
    num2 = 200

    def __init__(self, a, b):
        print("Child Constructor Calling...")
        Calculator.__init__(self, a, b)

    def getCompleteData(self):
        return self.num1 + self.num + self.addition()


child_object1 = ChildCalculator(2, 10)
print(child_object1.getCompleteData())
