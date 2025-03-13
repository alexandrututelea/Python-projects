def add(n1, n2):
    return n1 + n2
def substract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1 / n2
operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}
def calculator():
    continue_calculation = True
    num1 = float(input("What is the first number?: "))
    while continue_calculation:
        for symbol in operation:
            print(symbol)
        operator = input("What is the operation?: ")
        num2 = float(input("What is the second number?: "))
        result = operation[operator](num1,num2)
        user_choice = input(f"Do you want to continue calculation with {result}?(yes/no): ")

        if user_choice == "yes":
            num1 = result
            print(f"First number is {result}")
        else:
            continue_calculation = False
            calculator()
calculator()