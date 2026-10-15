#program for assignment operators 
a = int(input("Enter a number: "))

print("Initial value:", a)

a += 5
print("After addition assignment:", a)

a -= 2
print("After subtraction assignment:", a)

a *= 3
print("After multiplication assignment:", a)

a /= 2
print("After division assignment:", a)

a = int(a)
a //= 2
print("After floor division assignment:", a)

a %= 3
print("After modulus assignment:", a)

a **= 2
print("After exponentiation assignment:", a)
