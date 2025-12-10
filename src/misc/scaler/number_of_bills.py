'''
Problem Description

Given total bills amount and amount of a single bill. Print number of bills.
Input Format

The first line contains a real number N denoting the total budget.
The second line contains an integer M denoting the value of a single bill.
Output Format

Print in a single line denoting the total number of bills that can fit in the total budget.

'''
'''
Example Explanation:

Here, the bill amount is 126.3 and the value of a single bill is 5. 
Hence, total number of bills that can fit in the total budget as whole number, 
will be 126.3 divided by 5 which returns 25.
Note: The problem constraints mean that when we test your code, the test cases used in the backend can have input values only within those constraints. You need not implement them in your code. You need to make sure your code will work for all such input values!
'''
N=float(input())
M=int(input())
bills=N//M
print(int(bills))