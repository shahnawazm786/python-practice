# Question 4: A system tracks performance scores of interns over 3 months. Based on the rules:

# The final score is calculated using this logic:
# final_score = (month1 + month2 * 2 - month3 // 2) ** 2 % 10
# If the intern’s final score is greater than 4 and even, label them 'GREAT'
# If the score is less than 5 or odd, label them 'AVERAGE'
# If the score is exactly 5, label 'CONFUSING'
# You have to read all 3 scores using input() and decide the label.

# Sample Input:
# 5
# 4
# 3

# Sample Output:
# AVERAGE



month1=int(input("enter month1"))
month2=int(input("enter month2"))
month3=int(input("enter month3"))
final_score=(month1 + month2 * 2 - month3 //2 ) ** 2 % 10
print(final_score)
if final_score>4 and final_score%2==0:
    print('GREATE')
elif final_score==5:
    print('CONFUSING')
else:
    print('AVERAGE')