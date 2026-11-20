# program for list in dynamic input values 

numbers = []

n = int(input("How many numbers? "))

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

print("List:", numbers)
print("First element:", numbers[0] if numbers else "Empty list")
print("Total elements:", len(numbers))
print("Sum:", sum(numbers))
