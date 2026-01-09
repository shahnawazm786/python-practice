"""
Problem Statement:

Given the start, end, and the stepsize return a numpy array sequence in given range with the specified stepsize.
Input Format:

One line of input will have 3 space-separated numbers consisting of start, end of sequence and step.
Output Format:

A numpy array with elements rounded off to 2 decimal places.
Sample Input:

5 7 0.5
Sample Output:

[5 5.5 6 6.5]
Note: To round off the numpy array, use np.round()

P.s: Recall that we can have float step size in numpy array

"""
import numpy as np

arr=np.arange(5,10,.5)
print(arr)