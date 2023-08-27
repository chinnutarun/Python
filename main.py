#calculator
from art import logo

def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


#dictonaries

operations = {"+": add, "-": sub, "*": mul, "/": div}


def calculator():
    print(logo)
    num1 = float(input("What is first number: "))
    num2 = float(input("What is second number: "))
    for i in operations:
        print(i)
    operator = input("what is the operator: ")
    ans = operations[operator](num1, num2)
    print(ans)
    inp = input(
        f"type 'y' to continue calculating with {ans}, or       type 'n' to exit.: "
    )
    if inp == "y":
        while inp == "y":
            operator = input("pick an operation: ")
            num1 = ans
            num2 = float(input("What is next number: "))
            ans = operations[operator](num1, num2)
            print(ans)
            inp = input(
                f"type 'y' to continue calculating with {ans},         or type 'n' to exit.: "
            )

    perform = input("Do you want to perform new calculation 'Yes'or 'No': ")
    if perform == "Yes":
        calculator()
    else:
        return


calculator()
