class calculator:

    def __init__(self):
        self.number1=float(input("enter your number 1"))
        self.number2=float(input("enter your number2"))

    def addition(self):
        addition=self.number1+self.number2
        print("the additon is",addition)

    def subtraction(self):
        subtraction=self.number1-self.number2
        print("the subraction is",subtraction)

    def multiplication(self):
        multiply=self.number1*self.number2
        print("the multiplication is",multiply)

    def divide(self):
        divide=self.number1/self.number2
        print("the division is",divide)
obj1=calculator()
obj1.addition()
obj1.subtraction()
obj1.multiplication()
obj1.divide()
