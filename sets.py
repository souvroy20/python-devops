data = {"john", "doe", 53.44}
print(type(data))

data2 = ["john", "doe", 53.44]
print(type(data2))

data_set = set(data2)
print(data_set)

data_dict = {'name': 'suresh', 'age': 22,
             'city': 'chennai', 'state': 'tamilnadu'}
valuee = set(data_dict)
value_set = set(data_dict.values())
print(valuee)
print(value_set)
print(data_dict.get('name'))
