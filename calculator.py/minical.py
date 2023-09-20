def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def clear():
    global history

    history = []


def history_list():
    print("History:")

    for expression in history:
        print(expression)


def main():
    global history

    history = []

    while True:

        operation = input("Select operation (1. Add, 2. Subtract, 3. Multiply, 4. Divide, 5. History, 6. Exit): ")

        if operation == "1":

            a = float(input("Enter first number: "))

            b = float(input("Enter second number: "))

            result = add(a, b)

            print(f"{a} + {b} = {result}")

            history.append(f"{a} + {b} = {result}")



        elif operation == "2":

            a = float(input("Enter first number: "))

            b = float(input("Enter second number: "))

            result = subtract(a, b)

            print(f"{a} - {b} = {result}")

            history.append(f"{a} - {b} = {result}")



        elif operation == "3":

            a = float(input("Enter first number: "))

            b = float(input("Enter second number: "))

            result = multiply(a, b)

            print(f"{a} * {b} = {result}")

            history.append(f"{a} * {b} = {result}")



        elif operation == "4":

            a = float(input("Enter first number: "))

            b = float(input("Enter second number: "))

            result = divide(a, b)

            print(f"{a} / {b} = {result}")

            history.append(f"{a} / {b} = {result}")



        elif operation == "5":


            print(history)



        elif operation == "6":

            break



        else:

            print("Invalid operation.")


if __name__ == "__main__":
    main()
