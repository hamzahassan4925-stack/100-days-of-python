Vdef (x, y)
x + y

 subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Zero se divide nahi kar sakte."
    return x / y

def calculator():
    print("--- Python Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Option chunen (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Pehla number likhen: "))
            num2 = float(input("Doosra number likhen: "))
        except ValueError:
            print("Ghalt input! Sirf numbers enter karen.")
            return

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Ghalt option chunain!")

if __name__ == "__main__":
    calculator()