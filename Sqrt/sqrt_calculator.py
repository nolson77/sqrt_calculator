import math # Import the math library for the square root function

print("Square Root Calculator (type 'q' to quit)")

while True:
    user_input = input("Enter a number or 'q' to quit): ")

    if user_input.lower() == 'q':
        print("Goodbye!")
        break

    try:
        number = float(user_input)
        if number >= 0:
            print(f"The square root of {number} is {math.sqrt(number):.4f}")
        else: print("Square root not defined for negative numbers in real numbers.")
    except ValueError:
        print("Please enter a valid number or 'q'.")
        