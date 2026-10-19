
# program for all python operators in one single code by using functions 

def operators():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Arithmetic operators
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
    print("Exponent:", a ** b)

    # Comparison operators
    print("Equal:", a == b)
    print("Not Equal:", a != b)
    print("Greater Than:", a > b)
    print("Less Than:", a < b)
    print("Greater or Equal:", a >= b)
    print("Less or Equal:", a <= b)

    # Assignment operator
    c = a
    c += b
    print("Addition Assignment:", c)

    # Logical operators
    print("Logical AND:", a > 0 and b > 0)
    print("Logical OR:", a > 0 or b > 0)
    print("Logical NOT:", not (a > 0))

    # Membership operators
    numbers = [10, 20, 30, 40]
    print("10 in numbers:", 10 in numbers)
    print("50 not in numbers:", 50 not in numbers)

    # Identity operators
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]
    print("x is y:", x is y)
    print("x is z:", x is z)

operators()
