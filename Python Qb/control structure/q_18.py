import random
import string
print("Generate a random alphabetical character:")
print(random.choice(string.ascii_letters))
print("\nGenerate a random alphabetical string:")
max_length=6
s=""
for i in range(random.randint(1,max_length)):
    s+=random.choice(string.ascii_letters)
print(s)
print("Generate a random alphabetical string of a fixed length:")
s=""
for i in range(10):
    s+=random.choice(string.ascii_letters)
print(s)
