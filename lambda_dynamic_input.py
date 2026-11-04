
# program for lambda function with dynamic input values
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y

print("Addition:", add(a, b))
print("Subtraction:", sub(a, b))
print("Multiplication:", mul(a, b))
