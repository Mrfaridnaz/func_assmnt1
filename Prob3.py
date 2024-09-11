# 3. How are lambda functions typically used in Python? Provide an example use case.
# Explanation in text3

# 1. Using lambda with sorted():
# You can use a lambda function to sort a list of tuples based on a specific element.

# List of tuples
students = [("John", 85), ("Emma", 92), ("Harry", 78), ("Olivia", 89)]

# Sorting based on the second element (grades)
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
print(sorted_students)

# 2. Using lambda with map():
# The map() function applies a function to each item of an iterable.
# A lambda function can be used to create this function inline.

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Doubling each number using map() and a lambda function
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)

# Using lambda with filter():
# You can use a lambda function with filter() to select certain elements from a list based on a
# condition.

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Filtering out even numbers using a lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# 4. Using lambda with reduce():
# The reduce() function (from the functools module) reduces a list to a single value by applying
# a function cumulatively to the elements. Lambda functions are often used here for concise expressions.

from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]

# Summing all numbers using reduce() and a lambda function
total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)
