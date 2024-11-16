# Take input for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Print the numbers before swapping
print("\nBefore swapping:")
print("First number:", num1)
print("Second number:", num2)

# Swap the numbers using Python's tuple unpacking
num1, num2 = num2, num1

# Print the numbers after swapping
print("\nAfter swapping:")
print("First number:", num1)
print("Second number:", num2)