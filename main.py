import math

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

mode = input("Enter the mode (+, -, *, /): ")

match mode:
    case "+":
        result = num1 + num2
        print(f"The result is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result is: {result}")
    case "/":
        if num1 or num2 == 0:
            print('Incorrect input')
            exit()
        else:
            result = num1 / num2
            print(f"The result is: {result}")

