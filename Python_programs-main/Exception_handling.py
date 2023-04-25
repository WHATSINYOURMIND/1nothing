# Handling exceptions in python
try:
    age = int(input("ENTER YOUR AGE: "))
    inc = 20000
    risk = inc/age
    print(age)
except ZeroDivisionError:
    print('age cannot be zero.')
except ValueError:
    print('invalid value')

# try this
# can put in a while loop and execute it until proper age is entered

# 0 means success of program
# 1 means program crashed

