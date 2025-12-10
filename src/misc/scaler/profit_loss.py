'''
Problem Description

You are given the Cost Price C and Selling Price S of a Product. You have to tell whether there is a Profit or Loss. Also, calculate total profit or loss.

NOTE: It is guaranteed that Cost Price and Selling Price are not equal.

NOTE: You have to take input of the Cost Price(C) and Selling Price(S) from the user.

Example Explanation

Explanation 1:

 Cost Price = 2
 Selling Price = 4
 As Cost Price < Selling Price, there is a profit.
 Total Profit = Selling Price - Cost Price = 4 - 2 = 2
Explanation 2:

 Cost Price = 4
 Selling Price = 1
 As Cost Price > Selling Price, there is a loss.
 Total Loss = Cost Price - Selling Price = 4 - 1 = 3 

'''


C=int(input())
S=int(input())
if C<S:
    print(1)
else:
    print(-1)

print(abs(C-S))
