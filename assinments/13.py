def   print_numbers_in_descending_order(num1,num2,num3):
#Create a list with the three numbers
     numbers=[num1,num2,num3]
#Sort the list in descending order
     numbers.sort(reverse=true)
#print the numbers in descending order
    print("Numbers in descending order:",numbers[0],numbers[1],numbers[2])
# Example usage
    num1=int(input("Enter the first number:" ))
    num2=int(input("Enter the second number:" ))
    num3=int(input("Enter the third number:" ))
# Call the function to print the numbers in descending order
  print_numbers_in_descending_order(num1, num2, num3)