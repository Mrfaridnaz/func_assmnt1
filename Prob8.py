# Implement a lambda function to filter out all the even numbers from a list of integers.


# Lambda function to filter out even numbers
filter_even = lambda lst: list(filter(lambda x: x % 2 == 0, lst))

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_even(numbers)
print(result)  # Output: [1, 3, 5, 7, 9]

# 9 ----------------------------------------------------
# Write a lambda function to sort a list of strings in ascending order based on the length of each
# string.
# Lambda function to sort strings based on their length

sort_by_length = lambda lst: sorted(lst, key=lambda x: len(x))

# Example usage
strings = ["apple", "banana", "kiwi", "grape", "pineapple"]
result = sort_by_length(strings)
print(result)

# 10 -------------------------------------------------------------
# Create a lambda function that takes two lists as input and returns a new list containing the
# common elements between the two lists.

# Lambda function to find common elements between two lists

common_elements = lambda lst1, lst2: list(filter(lambda x: x in lst2, lst1))
# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = common_elements(list1, list2)
print(result)  # Output: [4, 5]

# 11 -------------------------------------------------------------
# Write a recursive function to calculate the factorial of a given positive integer.

# Recursive function to calculate factorial
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}")  # Output: 120


# 12 -------------------------------------------------------------
# Recursive function to calculate the nth Fibonacci number
def fibonacci(n):
    # Base case: Return n if it's 0 or 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: Fibonacci of (n-1) + Fibonacci of (n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = 6
result = fibonacci(n)
print(f"The {n}th Fibonacci number is {result}")

# 13 -------------------------------------------------------------
# Create a recursive function to find the sum of all the elements in a given list.

def sum_list(lst):
    # Base case: empty list
    if not lst:
        return 0
    # Recursive case: sum of the first element and the sum of the rest of the list
    else:
        return lst[0] + sum_list(lst[1:])

# Example usage
numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print(f"The sum of the list is {result}")

# 14 -------------------------------------------------------------
# Write a recursive function to determine whether a given string is a palindrome.

def is_palindrome(s):
    # Base case: a single character or empty string is a palindrome
    if len(s) <= 1:
        return True
    # Check if the first and last characters are the same
    elif s[0] != s[-1]:
        return False
    # Recursive case: check the substring without the first and last characters
    else:
        return is_palindrome(s[1:-1])

# Example usage
string = "racecar"
result = is_palindrome(string)
print(f"'{string}' is a palindrome: {result}")

# 15 -------------------------------------------------------------
# Recursive function to find the GCD of two positive integers
def gcd(a, b):
    # Base case: if b is 0, GCD is a
    if b == 0:
        return a
    # Recursive case: GCD of b and a % b
    else:
        return gcd(b, a % b)

# Example usage
num1 = 48
num2 = 18
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")  # Output: 6
