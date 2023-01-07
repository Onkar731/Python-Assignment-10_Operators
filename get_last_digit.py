"""
Write a python script to get the last digit from a given number
(for example, if user enters 2089 then your output should be 9)
"""

# taking input from the user
num = int(input("Enter a number : "))

# getting last digit from the given number by using arithmetic modulo operator
num_last_digit = num % 10

# printing last digit of the given number
print("Last digit of the", num, "is", num_last_digit)

# print("Last digit of the %d is %d" %(num, num_last_digit))