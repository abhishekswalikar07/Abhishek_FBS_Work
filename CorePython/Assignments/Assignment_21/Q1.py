

def calculate(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            try:
                return num1 / num2
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                return None
        else:
            raise ValueError("Invalid Operator")
    except ValueError as ve:
        print(f"Error: {ve}")
        return None

while True:
    print("\n--- Simple Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting the calculator. Goodbye!")
        break

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        
        if choice == '1':
            operator = '+'
        elif choice == '2':
            operator = '-'
        elif choice == '3':
            operator = '*'
        elif choice == '4':
            operator = '/'
        else:
            print("Error: Invalid menu choice.")
            continue

        result = calculate(num1, num2, operator)
        if result is not None:
            print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Error: Invalid number entered. Please enter numeric values only.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
