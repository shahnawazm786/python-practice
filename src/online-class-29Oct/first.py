# Question 2:

# Context:

# You are given three inputs from the user. The goal is to find the average,
# but the input must be taken as strings and converted to integers without using any method except int()
# and input(). Finally, print the average rounded to 2 decimal places using only print() and basic operators.

# Task:

# Write a program that:

# Takes 3 inputs using input().
# Converts them to integers using int().
# Calculates the average.
# Prints the average in the format:
# Average of the three numbers is:
# where is rounded to 2 decimal places using print() formatting only.
# You cannot use round() or format() methods. Just use print() smartly.

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter second number"))
#average=round((a + b + c/3),2)
average=(a+b+c)/3
print (f"first number {a} and second number {b} and third number {c} and average is {average:.4f}")