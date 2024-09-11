# Are lambda functions in Python able to access variables defined outside of their own scope?
# Explain with an example.

# yes, lambda functions in Python can access variables defined outside of their own scope.
# This behavior is due to closures in Python, which allow the lambda function to capture and
# remember the environment in which they were created, even after that environment has gone out of scope.
# Example: Accessing Variables Outside Lambda Scope.

# Variable defined in the outer scope
multiplier = 2

# Lambda function accessing the outer variable
double = lambda x: x * multiplier

# Using the lambda function
result = double(5)
print(result)  # Output: 10

# This ability to access external variables is part of Python’s lexical scoping
# (also known as static scoping), where a function or lambda "remembers" the variables from the
# environment in which it was defined.
# ---------------------------------------------------
# Example: Lambda in a Function (Closure)
def make_multiplier(n):
    # Lambda function that remembers 'n' from the outer scope
    return lambda x: x * n

# Create a function that multiplies by 3
times_three = make_multiplier(3)

# Using the closure
result = times_three(4)
print(result)  # Output: 12

# Key Takeaway:
# Lambda functions (like regular functions) can access variables from their enclosing scope
# (outer function or global scope).
# This behavior is useful in many cases, such as creating function factories or using lambdas in callbacks.