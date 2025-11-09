def add_sprinkles(func):
    def wrapper(*args, **kwargs): #this wrapper makes sure that add_sprinkles isn't executed directly without get_ice_cream being called
        print(f'You have added sprinkles')
        func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print(f'You have added fudge')
        func(*args, **kwargs)

    return wrapper


@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f'Here is your {flavor} ice cream!')


get_ice_cream('vanilla')
