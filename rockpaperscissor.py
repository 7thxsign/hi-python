import random

moves = ('rock', 'paper', 'scissor')

game_running = True

while game_running:
    player_move = None
    computer_move = random.choice(moves)

    while player_move not in moves:
        player_move = input('Enter your move (Rock, Paper, Scissor): ').lower()

    print(f'You picked: {player_move}')
    print(f'The computer picked: {computer_move}')

    if player_move == computer_move:
        print('Draw')
    elif player_move == 'rock' and computer_move == 'scissor':
        print('You win!')
    elif player_move == 'paper' and computer_move == 'rock':
        print('You win!')
    elif player_move == 'scissor' and computer_move == 'paper':
        print('You win!')
    else:
        print('You lose!')

    # play_again = input('Do you want to play again? (y/n): ').lower()
    # if play_again == 'n':
    #     print('Thank you for playing!')
    #     game_running = False

    play_again = input('Do you want to play again? (y/n): ').lower()
    if not play_again == 'y':
        print('Thank you for playing!')
        game_running = False