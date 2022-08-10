score = 0

# Question 1
answer1 = input('What is the capital of India? \n (a) Mumbai \n (b) Delhi \n (c) Madras \nAnswer: ')
if answer1 == 'b' or answer1 == 'Delhi':
    print('Correct!')
    score += 1
    print('Score: ', score)
    print('\n')
else:
    print('Incorrect! The answer is Delhi')
    print('score: ', score)
    print('\n')

# Question 2
answer2 = input ('What is the capital of Maharashtra state? \n (a) Nagpur \n (b) Pune \n (c) Mumbai \nAnswer: ')
if answer2 == 'c' or answer2 == 'Mumbai':
    print('Correct!')
    score += 1
    print('score: ', score)
    print('\n')
else:
    print('Incorrect! Answer is Mumbai')
    print('score: ', score)
    print('\n')

# Final Message
if score == 0:
    print('Your total score is:',score, '\nyou suck!')
elif score == 1:
    print('Your total score is:',score , '\nyou done ok!')
else:
    print('Your total score is:',score , '\nyou done excellent!')







