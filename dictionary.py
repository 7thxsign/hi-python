capitals = {'India':'New Delhi',
            'Japan':'Tokyo',
            'United States':'Washington DC',
            'South Korea':'Seoul',}

print(capitals.get('Japan'))

if 'China' in capitals:
    print('China exists')
else:
    print('China doesn\'t exist')