# Question 6: A security system classifies users based on their login attempts and access level. Each user provides two inputs:

# Number of login attempts: attempts (integer)
# Access level: level (integer: 1=Guest, 2=User, 3=Admin)

# Rules:
# If attempts > 3 and level == 1: print "Access Denied"
# If attempts <= 3 and level is Admin: print "Welcome, Admin"
# If attempts == 0 and level is User or Admin: print "New Session"
# If attempts > 5: print "Security Alert" regardless of level
# Use correct indentation and structure
# Write a program that implements this logic accurately, ensuring no unnecessary nesting or logic flaws.

# Sample Input 1:
# 2
# 3

# Sample Output 1:
# Welcome, Admin

# Sample Input 2:
# 6
# 2

# Sample Output 2:
# Security Alert

attempt=int(input('enter attempt'))
level=input('enter level')
if attempt>3 and level==1:
    print("Access denied")
elif attempt<=3 and level=='Admin':
    print('Welcome, Admin')

