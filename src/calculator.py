# src/calculator.py

class Calculator:
    """Simple calculator with basic operations."""
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            return a / b

# print(Calculator.multiply(Calculator,1,2))
