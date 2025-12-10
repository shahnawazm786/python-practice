'''
Problem Description

Given total bills amount and amount of a single bill. Print number of bills.
Input Format

The first line contains a real number N denoting the total budget.
The second line contains an integer M denoting the value of a single bill.
Output Format

Print in a single line denoting the total number of bills that can fit in the total budget.

'''
N=float(input())
M=int(input())
bills=N//M
print(bills)