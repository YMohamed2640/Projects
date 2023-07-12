# Simple calculator
def add(x, y):
    """Adds two numbers"""
    sum = x + y
    return sum

def subtract(x, y):
    """Subtracts two numbers"""
    diff = x - y
    return diff

def multiply(x, y):
    """Multiplies two numbers"""
    product = x*y
    return product

def divide(x, y):
    """Divides two numbers"""
    q = x/y
    return q


def power(x, y):
    """x ^ y"""
    r = x ** y
    return r


while True:
    valid_r = ["y", "n"]
    o = input("Enter operation (1. Multiply, 2. divide, 3. add, 4. subtract, 5. power) ").lower()
    operations = ["multiply", "divide", "add", "subtract", "power"
                    "1", "2", "3", "4", "5"]

    while o not in operations:
        print("Invalid operation. ")
        o = input("Enter operation (1. Multiply, 2. divide, 3. add, 4. subtract, 5. power) ").lower()
        if o in operations:
            break
        
    if o == "subtract":
        x = int(input("Enter first no. "))
        y = int(input("Enter second no. "))
        print(subtract(x, y))

    elif o == "add":
        x = int(input("Enter first no. "))
        y = int(input("Enter second no. "))
        print(add(x, y))

    elif o == "divide":
        x = int(input("Enter first no. "))
        y = int(input("Enter second no. "))
        while y == 0:
            print("Math error.")
            y = int(input("Enter second no. "))
            if y != 0:
                break
        print(divide(x, y))

    elif o == "power":
        x = int(input("Enter first no. "))
        y = int(input("Enter second no. "))
        print(power(2, 3))

    else:
        x = int(input("Enter first no. "))
        y = int(input("Enter second no. "))
        print(multiply(x, y))


    r = input("Do you want to restart the calculator? ").lower()
    while r not in valid_r:
        print("Invalid input")
        r = input("Do you want to restart the calculator? ").lower()
        if r in valid_r:
            break
    if r != "y":
        break