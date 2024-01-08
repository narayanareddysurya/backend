def is_three_digit_number(number):
    if 100 <= number <= 999:
        return True
    else:
        return False

# Example usage:
 user_input = int(input("Enter a number: "))

 if is_three_digit_number(user_input):
    print(f"{user_input} is a 3-digit number.")
 else:
    print(f"{user_input} is not a 3-digit number.")
