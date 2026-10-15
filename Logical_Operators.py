#program for logical operators

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Both numbers are positive:", a > 0 and b > 0)

print("At least one number is positive:", a > 0 or b > 0)

print("First number is not positive:", not (a > 0))
