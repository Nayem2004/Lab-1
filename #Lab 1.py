#Lab 1

class SimpleCalculator:
    def __init__(self):
        self.result = 0

    def add(self, value):
        self.result += value
        return self.result

    def subtract(self, value):
        self.result -= value
        return self.result

    def multiply(self, value):
        self.result *= value
        return self.result

    def divide(self, value):
        if value != 0:
            self.result /= value
        else:
            return "Error: Division by zero!"
        return self.result

    def clear(self):
        self.result = 0
        return self.result

    def get_result(self):
        return self.result

def main():
    calculator = SimpleCalculator()

    print("Simple Calculator")
    print("Enter 'exit' to quit")
    print("Operations: add, subtract, multiply, divide, clear")

    while True:
        operation = input("Enter operation: ").lower()

        if operation == "exit":
            break
        elif operation == "clear":
            calculator.clear()
            print(f"Result: {calculator.get_result()}")
        elif operation in ("add", "subtract", "multiply", "divide"):
            try:
                value = float(input("Enter value: "))
                if operation == "add":
                    print(f"Result: {calculator.add(value)}")
                elif operation == "subtract":
                    print(f"Result: {calculator.subtract(value)}")
                elif operation == "multiply":
                    print(f"Result: {calculator.multiply(value)}")
                elif operation == "divide":
                    print(f"Result: {calculator.divide(value)}")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Invalid operation.")

main()
