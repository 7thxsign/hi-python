def add(*args): #it is used to pass multiple arguments as tuples using *
    total = 0
    for arg in args:
        total += arg
    print(f'The total is: {total}')

# add(1,2)

def display_name(*args):
    for arg in args:
        print(arg, end=' ')

# display_name('Dr.','Hello','world','III')

def print_address(**kwargs):  #it is used to pass multiple arguments as a dictionary using **
    for key, value in kwargs.items():
        print(f'{key}: {value}')

# print_address(street='1234 Fake St.',
#               city='Detroit',
#               state='MI',
#               zip='128973')

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')

    print()

    if 'apt' in kwargs:
        print(f'{kwargs.get('street')} {kwargs.get('apt')}')
    else:
        print(f'{kwargs.get('street')}')
    print(f'{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}')


shipping_label('Dr.','Hello','world','III',
               street='1234 Fake St.',
               apt='#100',
               city='Detroit',
               state='MI',
               zip='128973')