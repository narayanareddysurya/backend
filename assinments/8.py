import sys

def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <number>")
        sys.exit(1)

    # Get the number from the command-line argument
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer.")
        sys.exit(1)

    result = check_even_or_odd(num)
    print(f"The number {num} is {result}.")
