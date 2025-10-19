
foods = []
prices = []
total = 0

while True:
    food = input("Enter the foods you want (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)
        total += price

print('---------Cart----------')
print('-----------------------')

for food, price in zip(foods, prices):
    print(f'{food}: ${price:.2f}')

print('-----------------------')
print(f'Total: ${total:.2f}')
