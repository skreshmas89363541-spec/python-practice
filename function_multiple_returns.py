
# program for function with multiple return values 

def calculate(a, b):
    return a + b, a - b, a * b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add, sub, mul = calculate(a, b)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
