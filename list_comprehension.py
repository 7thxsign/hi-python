doubles = [x * 3 for x in range(1, 11)]
print(doubles)

fruits = ['apple', 'banana', 'orange', 'strawberry']
uppercase_fruits = [fruit.upper() for fruit in fruits]
first_uppercase_fruit = [fruit[0].upper() for fruit in fruits]
print(uppercase_fruits)
print(first_uppercase_fruit)

numbers = [1, -2, 3, -4, 5, -6, -7, 8, 9, -10]

positive_numbers = [num for num in numbers if num > 0]
print(positive_numbers)
