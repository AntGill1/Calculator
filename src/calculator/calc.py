# Create simple calculator app

class Calculator:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        if num2 == 0:
            raise ArithmeticError
        return num1 / num2

    
