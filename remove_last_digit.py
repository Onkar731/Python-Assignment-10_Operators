"""
Write a python script to remove the last digit from a given number.
(for example, if user enters 2534 then your output should be 253)
"""

# taking input from the user
num = int(input("Enter a number : "))

# removing last digit by floor division
without_last_digit = num // 10

# printing digit without last digit
print(num, "is without last digit =>", without_last_digit)

# print("%d is wihtout last digit => %d" %(num, without_last_digit))

