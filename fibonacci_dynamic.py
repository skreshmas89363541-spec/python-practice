# program for Fibonacci dynamic

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

count = int(input("Enter number of terms: "))

if count < 0:
    print("Enter a non-negative number")
else:
    for i in range(count):
        print(fibonacci(i), end=" ")
