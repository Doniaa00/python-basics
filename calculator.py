def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "division by zero is not allowed"
    return a / b


def calculator():
    while True:
        print("\n=== calculator ===")
        print(" 1 add")
        print(" 2 subtract")
        print(" 3 multiply")
        print(" 4 divide")
        print(" 5 exit")
        choice = input("choose your option: ")

        if choice == "5":
            print("exit calculator")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("please try again.")
            continue

        try:
            num1 = float(input("enter first number: "))
            num2 = float(input("enter second number: "))
        except ValueError:
            print("please enter numbers only.")
            continue

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

        print("result:", result)


if __name__ == "__main__":
    calculator()

