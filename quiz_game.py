questions = (('Which keyword is used to exit a loop in Python?'),
             ('What is the output of 3 % 60 in Python?'),
             ('Which data type is used to store a sequence of elements?'),
             ('What does zip() function do in Python?'),
             ('Which symbol is used for comments in Python?'))
options = (
    ('A. exit', 'B. quit', 'C. break', 'D. stop'),         # Q1
    ('A. 0', 'B. 3', 'C. 57', 'D. Error'),                 # Q2
    ('A. int', 'B. float', 'C. list', 'D. bool'),          # Q3
    ('A. Compress files', 'B. Combine iterables', 'C. Sort items', 'D. End a loop'),  # Q4
    ('A. //', 'B. #', 'C. *', 'D. %')                     # Q5
)

answers = ('C','B','C','B','B')
guesses = []
score = 0
question_number = 0

for question in questions:
    print('-------------------------')
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input(print('Enter your options (A, B, C, D): ')).upper()
    guesses.append(guess)
    if guess == answers[question_number] :
        print('Correct!')
        score += 1
    else:
        print('Incorrect!')

    question_number += 1
print(f'Your score was: {score}')

