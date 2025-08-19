# Program to generate Fibonacci numbers
# Enter the number of terms to generate
n = int(input("Enter the number of terms: "))

# First two Fibonacci numbers
a, b = 0, 1

print("Fibonacci sequence:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
