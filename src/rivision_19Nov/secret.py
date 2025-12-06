secret=5
guess=int(input('Guess a num :'))

if guess > secret :
    print('too high')
elif guess==secret:
    print('equal')
else:
    print('too low')