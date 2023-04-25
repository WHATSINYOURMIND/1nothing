# Lists
names = ['john', 'laksh', 'jay', 'shryea', 'manav']
names[3] = 'Shreya'
print(names[2])
print(names)
print(names[-1])
print(names[0:2])
print(names[1:])
print(names[:])

numbers = [3, 9, 4, 11, 21]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)

# 2D Lists
m = [
    [2, 3, 4],
    [1, 2, 3],
    [5, 6, 7]
]
print(m[0][2])

for row in m:
    for i in row:
        print(i, end=' ')
print()

# List method and functions
# append, insert, remove , clear , pop , index , sort , reverse
n = [2, 7, 9, 1, 0, 9, 3, 22]
print('before operations')
print(n)
n.append(25)
n.insert(1, 12)
n.remove(9)
print('after operations')
print(n)
n.sort()
print(n)


