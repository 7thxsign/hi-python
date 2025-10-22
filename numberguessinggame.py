import random

lowest_number = 1
highest_number = 100

answer = random.randint(lowest_number, highest_number)

guesses = 0

is_running = True

while is_running:
    guess = input(f'Take a guess between {lowest_number} and {highest_number}: ')
    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_number or guess > highest_number:
            print(f'Your guess is out of range. Try again.')
            print(f'Take a guess between {lowest_number} and {highest_number}: ')
        elif guess < answer:
            print(f'Your guess is too low.')
        elif guess > answer:
            print(f'Your guess is too high.')
        else:
            print(f'Your guess is correct!')
            print(f'Number of guesses: {guesses}')
            is_running = False

    else:
        print('Invalid input. Try again.')
        print(f'Please enter a number from {lowest_number} to {highest_number}.')