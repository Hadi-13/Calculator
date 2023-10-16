# CALCULLATOR.

# Add:
def add(n1, n2):
    return n1 + n2

# Subtract:
def subtract(n1, n2):
    return n1 - n2

# Multiply:
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

# this dictionary is goin to act as te means in which
# we are going to call these functions.

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# At some point, we want to  be able to tap into the operations
# and then pass in the key that we want

# operations["*"]

# and then stire this as the function that we want

# function = operations["*"]

# that means that we can call this function and then pass in one number
# and a second number

# function(2, 3)

# and this function is currently going to act as the multiply
# function.
def calculator():
    num1 = float(input("What's the first number?: "))
    # num2 = int(input("What's the second number?: "))

    # next we want to ask them which of these operations
    # they want to do.

    # @1: we want to loop through this dictionary and print
    #       out each of these keys, and ask the user to type out
    #       one of them so that we can figure out which operation
    #       they actually want to do.



    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)   # we are going to change it to firt answer.

        # if operation_symbol == "+":
        #     answer =  add(num1, num2)
        # elif operation_symbol == "-":
        #     answer = subtract(num1, num2)
        # elif operation_symbol == "*":
        #     answer = multiply(num1, num2)
        # else:
        #     answer = divide(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

