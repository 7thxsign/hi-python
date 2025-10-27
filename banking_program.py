def show_balance(balance):
    print(f'Your balance is: ${balance:.2f}')

def deposit():
    amount = float(input('How much do you want to deposit: '))
    if amount < 0:
        print('Invalid amount deposition.')
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input('How much do you want to withdraw: '))
    if amount > balance:
        print('Insufficient funds.')
        return 0
    elif amount < 0:
        print('Invalid amount withdraw.')
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print('Welcome to the banking program')
        print('Select an option:')
        print('1) Square balance')
        print('2) Deposit')
        print('3) Withdraw')
        print('4) Exit')
        choice = input("Enter your choice: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = balance + deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('Invalid choice')

    print('Thank you for using banking program')

if __name__ == '__main__':
    main()