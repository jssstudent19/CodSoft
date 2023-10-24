def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def factorial(x):
    if x < 0:
        return "Factorial is not defined for negative numbers"
    elif x == 0:
        return 1
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'power' for exponentiation")
    print("Enter 'factorial' for factorial")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("add", "subtract", "multiply", "divide", "power", "factorial"):
        if user_input == "factorial":
            num = int(input("Enter a number: "))
            print("Result: " + str(factorial(num)))
        else:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if user_input == "add":
                print("Result: " + str(add(num1, num2)))
            elif user_input == "subtract":
                print("Result: " + str(subtract(num1, num2)))
            elif user_input == "multiply":
                print("Result: " + str(multiply(num1, num2)))
            elif user_input == "divide":
                print("Result: " + str(divide(num1, num2)))
            elif user_input == "power":
                print("Result: " + str(power(num1, num2)))
    else:
        print("Invalid input. Please enter a valid operation.")
