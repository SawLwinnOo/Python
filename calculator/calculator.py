import operator


class Calculator:
    def __init__(self):
        self.operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def perform_operation(self, num1, num2, operator):
        if operator not in self.operations:
            return "Invalid operator"

        if operator == '/' and num2 == 0:
            return "Division by zero is not allowed"

        operation_func = self.operations[operator]
        result = operation_func(num1, num2)
        return result


def main():
    calc = Calculator()

    while True:
        print("Options:")
        print("Enter 'quit' to end the program.")
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == 'quit':
            break

        result = calc.perform_operation(num1, num2, operator)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
