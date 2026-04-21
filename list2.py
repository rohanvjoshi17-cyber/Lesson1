dict = {}

dict = {1: 'apple', 2: 'ball'}

dict = {'name': 'John', 1: [2, 4, 3]}

dict = {'name': 'Jack', 'age': 26}

print(dict['name'])
print(dict.get('age'))

dict['age'] = 27
print(dict)

dict['address'] = 'Downtown'
print(dict)

dict.pop('age')
print(dict)

print("Address :", dict.get('address'))

dict.clear()
print(dict)