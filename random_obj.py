import random
options = ('Rock', 'Paper', 'Scissor')
cards = ['2','4','5','6','7','8','9',]
option = random.choice(options)
number  = random.random() * 100
random.shuffle(cards)
print(option)
print(number)
print(cards)

