# collection based data types - list , tuples , dictionary and strings
# WE WILL SEE DICTIONARIES HERE

# Creation techniques
# Method 1 - with integer keys
d = {1: 'laksh', 2: 'doshi', 3: 'Legend'}
print(d)

# Method 2 - with mixed keys
d0 = {'name': 'laksh', 1: [1, 2, 3, 4]}
print(d0)

# Method 3 - using in built function
d1 = dict({1: 'LAKSH', 2: 'IS', 3: 'A', 4: 'SUPERSTAR'})
print(d1)

# method 4 - in pairs
Dict = dict([(1, 'rohit'), (2, 'Nehra')])
print("\nDictionary with each item as a pair: ")
print(Dict)

# ACCESSING ELEMENT FROM DICTIONARY - ITS DONE USING KEY VALUE
print(d[1])
print(d1.get(3))

# DELETING ELEMENT FROM A DICTIONARY
del(d1[4])
print(d1)
