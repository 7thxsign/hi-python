import random
import time

def spin_row():
    symbols = ['🔔','🍒','🍉','🍋','⭐']
    return [random.choice(symbols) for symbol in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        if row[0] == '🍉':
            return bet * 4
        if row[0] == '🍋':
            return bet * 5
        if row[0] == '🔔':
            return bet * 10
        if row[0] == '⭐':
            return bet * 20
    return 0

def main():
    balance = 100

    while balance > 0:
        print(f'Current balance is: ${balance:.2f}')
        bet = input('How much do you bet? ')
        if not bet.isdigit():
            print('Please enter a valid number.')
            continue

        bet = int(bet)

        if bet > balance:
            print('Sorry, you do not have enough money.')
            continue

        if bet <= 0:
            print('Please enter a valid bet.')
            continue

        balance -= bet

        row = spin_row()
        print('Spinning...')
        time.sleep(1)
        print('============')
        print_row(row)
        print('============')

        payout = get_payout(row, bet)

        if payout > 0:
            print(f'You won ${payout:.2f}!')
        else:
            print(f'Sorry, you lost this round!')

        balance += payout

        play_again = input('Would you like to play again? (Y/N): ').upper()

        if play_again != 'Y':
            break
    print('===========================================')
    print(f'Game over! Your balance is: ${balance:.2f}')
    print('===========================================')

if __name__ == '__main__':
    main()