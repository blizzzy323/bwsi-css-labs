"""
lab_1b.py

This is a script that implements a simple calculator.
"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            print("Cannot divide by zero.")
            return None
    else:
        print("Invalid operation.")
        return None


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Invalid number. Try again.")


def get_operation():
    while True:
        op = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()
        if op in ["add", "subtract", "multiply", "divide"]:
            return op
        else:
            print("Invalid operation. Try again.")


def main():
    print("===== Simple Calculator =====")

    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    result = simple_calculator(operation, num1, num2)

    if result is not None:
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()