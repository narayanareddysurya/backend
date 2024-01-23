 def reverse_digits(number):
 reversed_number=0
   while number >0:
    digit = number % 10
  reversed_number = reversed_number * 10 + digit
    number = number // 10
 return reversed_number
 num = int(input("Enter a number:"))
   result = reverse_digits(num)
  print(f"The reverse of {num} is: {result}")
    