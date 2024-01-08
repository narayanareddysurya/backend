def is_positive(number):
    if number > 0:
        return True
    else:
        return False

# Example usage:
user_input = float(input("Enter a number: "))  # Assuming the input can be a floating-point number

if is_positive(user_input):
    print(f"{user_input} is a positive number.")
else:
    print(f"{user_input} is not a positive number.")
