
# 1. Advantages of Lambda Functions:
# Concise Syntax: Lambda functions are written in a single line, making them useful for small,
# simple tasks. This helps in reducing code verbosity when a full function definition would be unnecessary.

# Example: lambda x, y: x + y
# is shorter than writing:
def add(x, y):
    return x + y
# 2.1 -----------------------------------
#
def example(x):
    if x > 0:
        return "Positive"
    else:
        return "Non-positive"

# 2.2 ------------------------------------
def example(x):
    """Returns 'Positive' if x > 0, else 'Non-positive'."""
    return "Positive" if x > 0 else "Non-positive"
# ------------------------------------

# No Annotations:
# Regular functions can include type hints or annotations to indicate expected input and output types,
# which helps in code clarity and debugging. Lambda functions cannot have annotations.

def add(x: int, y: int) -> int:
    return x + y
# 2.3 ---------------------------------------
# Lambda for simple operations
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# Regular function for more complex operations
def complex_operation(x, y):
    if x > 0 and y > 0:
        return x * y
    else:
        return x + y

print(complex_operation(3, 4))  # Output: 12
print(complex_operation(-1, 4))  # Output: 3
