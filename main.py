# Program demonstrating variables, data types, and if-else statements in Python

# 1. Variables and Data Types
# A variable is a container for storing data values. In Python, you don't need to declare the type of the variable beforehand.
# Python automatically assigns a data type based on the value.

# Integer variable
age = 25  # age is an integer

# Float variable
height = 5.9  # height is a floating point number (decimal)

# String variable
name = "Alice"  # name is a string (text)

# Boolean variable
is_student = True  # is_student is a boolean (True or False)

# 2. Printing the values
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# 3. Using If-Else Statements
# We use if-else statements to make decisions based on conditions.

# Check if age is greater than or equal to 18 (adulthood check)
if age >= 18:
    print(name + " is an adult.")
else:
    print(name + " is a minor.")

# Check if the person is a student
if is_student:
    print(name + " is a student.")
else:
    print(name + " is not a student.")

# 4. Combining multiple conditions
# We can also combine multiple conditions using 'and', 'or', and 'not'.

if age >= 18 and is_student:
    print(name + " is an adult and a student.")
elif age >= 18 and not is_student:
    print(name + " is an adult but not a student.")
else:
    print(name + " is not an adult.")
