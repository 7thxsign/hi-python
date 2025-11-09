
try:
    number = int(input('Enter a number: '))
    print(1 / number)
except ZeroDivisionError:
    print("Division by zero isn't allowed")
except ValueError:
    print("Numbers only brother :D")
finally:
    print('The code ends')