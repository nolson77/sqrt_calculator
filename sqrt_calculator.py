import math # Import the math library for the square root function

# get user input
number = float(input("Enter a number: "))

# Calculate square root (handle negative numbers simply)
if number >= 0:
    sqrt = math.sqrt(number)
    print(f"The square root of {number} is {sqrt}")
else: print("Square root not defined for negative numbers in real numbers.")
