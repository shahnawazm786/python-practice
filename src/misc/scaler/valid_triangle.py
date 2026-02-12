'''
Problem Description

You are given 3 integer angles(in degrees) A, B and C of a triangle. You have to tell whether the triangle is valid or not.


A triangle is valid if sum of its angles equals to 180.

NOTE: You have to take the input of 3 sides of triangle from the user.
'''
'''
Example Explanation

Explanation 1:



 Sum of angles = A + B + C = 60 + 60 + 60 = 180
 Hence, the given triangle is valid.
Explanation 2:

 Sum of angles = A + B + C = 30 + 40 + 50 = 120
 As sum of angles is not equal to 180, the given triangle is not valid.
'''
A=int(input())
B=int(input())
C=int(input())
if A + B + C ==180:
    print(1)
else:
    print(0)