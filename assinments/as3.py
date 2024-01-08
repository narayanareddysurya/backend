def is_divisible_by_seven(number):
    if number % 7 == 0:
        return True
    else:
        return False

# Example usage:
user_input = int(input("Enter a number: "))

if is_divisible_by_seven(user_input):
    print(f"{user_input} is divisible by 10.")
else:
    print(f"{user_input} is not divisible by 10.")
