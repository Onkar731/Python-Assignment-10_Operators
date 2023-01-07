"""
Write a python script which takes a three digit number form the user and
displays only its middle digit
"""

# taking input from the user
num = int(input("Ente a number : "))
temp = num

# getting middle digit of three digit number
num_middle_digit = (temp//10)%10

# printing middle digit of the given number
print("Middle digit of the", num, "is", num_middle_digit)

# print("Middle digit of the %d is %d" %(num, num_middle_digit))