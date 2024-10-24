import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero"

def exponentiate(x, y):
    return x ** y

def logarithm(x, base=math.e):
    try:
        return math.log(x, base)
    except ValueError:
        return "Error: Logarithm undefined for non-positive values"

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    try:
        return math.tan(math.radians(x))
    except ValueError:
        return "Error: Tangent undefined"

def advanced_calculation(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiate")
        print("6. Logarithm")
        print("7. Sine")
        print("8. Cosine")
        print("9. Tangent")
        print("10. Custom Calculation (e.g., sin(30) + log(10))")
        print("11. Exit")

        choice = input("\nEnter choice(1-11): ")

        if choice == '11':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")

        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")

        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")

        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")

        elif choice == '5':
            print(f"{num1} ^ {num2} = {exponentiate(num1, num2)}")

        elif choice == '6':
            num1 = float(input("Enter the number for logarithm: "))
            base = input("Enter base (leave blank for natural log): ")
            base = float(base) if base else math.e
            result = logarithm(num1, base)
            print(f"log({num1}) = {result}")

        elif choice == '7':
            angle = float(input("Enter angle in degrees: "))
            print(f"sin({angle}) = {sin(angle)}")

        elif choice == '8':
            angle = float(input("Enter angle in degrees: "))
            print(f"cos({angle}) = {cos(angle)}")

        elif choice == '9':
            angle = float(input("Enter angle in degrees: "))
            print(f"tan({angle}) = {tan(angle)}")

        elif choice == '10':
            expression = input("Enter your custom calculation (e.g., sin(30) + log(10)): ")
            result = advanced_calculation(expression)
            print(f"Result: {result}")

        else:
            print("Invalid input. Please choose a valid operation.")

if __name__ == "__main__":
    calculator()
