import time

def count(end, start=0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print('Done!')

#count(10)

def hello(greeting, title, first, last):
    print(f'{greeting} {title}{first} {last}')

hello('Hello','Mr.', last = 'Doe',first = 'John' )