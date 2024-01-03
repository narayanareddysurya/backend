# Read multiple values from the keyboard in a single line

# Input format: Enter values separated by space
input_str = input("Enter multiple values separated by space: ")

# Split the input string into a list of values
values = input_str.split()

# Convert the values to the appropriate data type (e.g., int or float)
# In this example, let's assume you're dealing with integers
int_values = [int(val) for val in values]

# Print the values
print("You entered:", int_values)
