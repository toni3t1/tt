def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return 'Error: Division by zero'
        else:
            return num1 / num2
    else:
        return 'Error: Invalid operation'
from arithmetic_operations import perform_operation

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ")

    result = perform_operation(num1, num2, operation)

    if isinstance(result, str) and 'Error' in result:
        print(result)
    else:
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()