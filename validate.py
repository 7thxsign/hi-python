def validate():
    username = input("Please enter your username: ")
    if len(username) > 12 or username.count(" ") > 0 or username.isalpha() == False:
        print('Invalid username')
    else:
        print('Valid username')
    return validate()

validate()