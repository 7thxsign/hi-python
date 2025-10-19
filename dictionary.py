capitals = {'India':'New Delhi',
            'Japan':'Tokyo',
            'United States':'Washington DC',
            'South Korea':'Seoul',}

print(capitals.get('Japan'))

if 'China' in capitals:
    print('China exists')
else:
    print('China doesn\'t exist')

capitals.update({'Germany':'Berlin'})
print(capitals)

capitals.pop('United States')
print(capitals)

keys = capitals.keys()
print(keys)

values = capitals.values()
print(values)

for value in values:
    print(value)