'''
Problem Statement:

Given a 1D array, return the first and last elements from the array.
Input Format: (NOTE : No need to take the input explicitly, the input-handling code is already in place.)

A 1D numpy array
Output Format:

A tuple (first_element, last_element)
Sample Input:

[0, 1, 2, 3, 4, 5]
Sample Output:

(0, 5)

'''
def get_element(arr):
    first_element=arr[0]
    last_element=arr[len(arr)-1]
    return (first_element,last_element)

print(get_element([0, 1, 2, 3, 4, 5]))