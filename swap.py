"""
Write a python script to swap data of two variables
"""

# taking input from the user
num1, num2 = int(input("Enter two numbers : ")), int(input())

# printing value before swapping
print("Before swapping : ", num1, num2)

# swapping data of two variables
temp = num1
num1 = num2
num2 = temp

# printing values after swapping
print("After swapping : ", num1, num2)

# print("After swapping : %d %d" %(num1,num2))