menu = {
    "pizza": 3.00,
    "nachos": 6.50,
    "burger": 5.00,
    "fries": 2.50,
    "taco": 3.50,
    "soda": 1.50,
    "water": 1.00,
    "ice cream": 2.75
}
cart = []
total = 0
print('==========MENU==========')
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print('========================')

while True:
    food = input('Enter your choice (q to quit): ')
    if food.lower() == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=' ')

print(f"The total is: {total}")