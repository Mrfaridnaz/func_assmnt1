# 1. What is a lambda function in Python,
# and how does it differ from a regular function?

# Explaination in test1 file

# Lambda function
# lambda arguments: expression
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

square = lambda x:x**2
print(square(3)) # Output: 9

# Regular function
def add(x, y):
    return x + y

print(add(2, 3))  # Output: 5


# Example with filter()
numbers = [1, 2, 3, 4, 5, 6]
# Using a lambda function to filter even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Equivalent with a regular function
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6]

