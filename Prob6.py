# Write a lambda function to calculate the square of a given number.

num = int(input("Enter any number : "))
sq = lambda x : x*x
result = sq(num)
print(f"This is the square of {num} : ", result)