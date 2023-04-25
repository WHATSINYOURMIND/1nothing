# modules - sections of packages which consist of functions which are used in making projects
# packages - corresponds to the packages in java
# it consists of several modules which are used in making projects
# there can be more than 100 modules which can be a program from addition of two numbers
# to creating various different sized buttons , boxes , in short interface
# python directories and package in a new program
# Each package consist of various modules

# syntax of getting a package :
# import packagename.modulename
import lak_learnings.calculator

print('Calculator program')
print('It will give you sum,diff,prod,remainder and quotient of two numbers')

print('for addition')
# syntax for getting function out of a module
# packagename.modulename.function_name
lak_learnings.calculator.add()

print('for product')
lak_learnings.calculator.prod()


# the following is the calculator program from the package lak_learnings.
# the package is imported in the above program and then we used the functions add and prod
def add():
    a = int(input('ENTER FIRST NUMBER'))
    b = int(input('ENTER SECOND NUMBER'))
    c = a + b
    print(c)


def sub():
    a = int(input('ENTER FIRST NUMBER'))
    b = int(input('ENTER SECOND NUMBER'))
    c = a - b
    print(c)


def prod():
    a = int(input('ENTER FIRST NUMBER'))
    b = int(input('ENTER SECOND NUMBER'))
    c = a * b
    print(c)


def division():
    a = int(input('ENTER FIRST NUMBER'))
    b = int(input('ENTER SECOND NUMBER'))
    c = a / b
    print(c)


def modulus():
    a = int(input('ENTER FIRST NUMBER'))
    b = int(input('ENTER SECOND NUMBER'))
    c = a % b
    print(c)
