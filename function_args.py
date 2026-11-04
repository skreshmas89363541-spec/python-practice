
# program for function arguments 
def add(*numbers):
    total = 0

    for n in numbers:
        total += n

    return total

print("Sum:", add(10, 20))
print("Sum:", add(10, 20, 30))
print("Sum:", add(5, 10, 15, 20))
