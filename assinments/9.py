import sys

def find_greatest_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <number1> <number2>")
        sys.exit(1)

    # Get the numbers from the command-line arguments
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Error: Please provide valid numeric values.")
        sys.exit(1)

    greatest_number = find_greatest_number(num1, num2)
    print(f"The greatest number between {num1} and {num2} is: {greatest_number}.")
s