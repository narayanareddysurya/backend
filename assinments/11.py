# Function to find and print and greatest numbr among three numbers
 dedef find_greatest_number(num1,num2,num3):
     greatest_number = max(num1,num2,num3)
      print(f"The greatest number is: {greatest_number}")
      
    # Example usage
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second mumber: "))
    number3 = float(input("Enter the  third number: "))
    
    find_greatest_number(number1, number2, number3)
    