"""
Write a python script which takes a three digit number from the user and
displays only its first digit
"""

# taking input from the user
num = int(input("Enter a three digit number : "))

# getting first digit from the number
num_first_digit = num // 100

# printing first digit of the number
print("First digit of the", num, "is", num_first_digit)

# print("First digit of the %d is %d" %(num, num_first_digit))