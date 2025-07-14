data = {'name': 'suresh', 'age': 22, 'city': 'chennai', 'state': 'tamilnadu'}
# print(data)
# print(data['name'])
# print(data['age'])
# print(data['city'])
# print(data['state'])
# print(data.keys())
# print(data.values())
# print(data.items())
# print(data.get('name'))

data['sex'] = 'Male'
print(data)
print(data.get('sex'))
del data['name']
print(data)
# print(data['name'])  # KeyError: 'name'# This will raise an error because ')
# print(data.get('age'))
# print(data.get('city'))
# print(data.get('state'))

# print(type(data))
# print(data.get('country', 'Not Found'))  # Default value if key doesn't exist

data2 = {
    'name': 'suresh',
    'age': 22,
    'city': 'chennai',
    'state': 'tamilnadu'
}
print(data2)
# print(data2['name'])
# print(data2['age'])
# print(data2['city'])
# print(data2['state'])
