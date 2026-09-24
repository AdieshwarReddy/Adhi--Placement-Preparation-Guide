# ============================================================
# 1. print() STATEMENT
# ============================================================

print()

# OUTPUT:
# A blank line is displayed.

Example with output

# ============================================================
# 2. PRINTING A STRING
# ============================================================

print("Hello")
print('Hello')

# OUTPUT:
# Hello
# Hello

# ============================================================
# 3. ESCAPE SEQUENCE CHARACTERS
# ============================================================

print("This is the\nfirst line")
print("This is the\tfirst line")
print("This is the \\nfirst line")

# OUTPUT:
# This is the
# first line
# This is the    first line
# This is the \nfirst line

# ============================================================
# 4. STRING REPETITION
# ============================================================

print(3 * "Hai")

# OUTPUT:
# HaiHaiHai

# ============================================================
# 5. STRING CONCATENATION
# ============================================================

print("City name=" + "Hyderabad")
print("City name=", "Hyderabad")

# OUTPUT:
# City name=Hyderabad
# City name= Hyderabad

# ============================================================
# 6. sep ATTRIBUTE
# ============================================================

a = 10
b = 20

print(a, b)
print(a, b, sep=",")
print(a, b, sep=":")
print(a, b, sep="----")

# OUTPUT:
# 10 20
# 10,20
# 10:20
# 10----20

# ============================================================
# 7. end ATTRIBUTE
# ============================================================

print("Hello", end="")
print("Dear", end="")
print("How are you?")

# OUTPUT:
# HelloDearHow are you?

# ============================================================
# 8. PRINTING OBJECTS
# ============================================================

my_list = [10, "A", "Hai"]
print(my_list)

my_tuple = (10, 20, 30)
print(my_tuple)

my_dictionary = {
    "Idly": 30.00,
    "Roti": 45.00,
    "Chappati": 55.50
}

print(my_dictionary)

# OUTPUT:
# [10, 'A', 'Hai']
# (10, 20, 30)
# {'Idly': 30.0, 'Roti': 45.0, 'Chappati': 55.5}

# ============================================================
# 9. PRINTING VARIABLES
# ============================================================

a = 2

print(a, "is an even number")
print("You typed", a, "as input")

# OUTPUT:
# 2 is an even number
# You typed 2 as input

# ============================================================
# 10. FORMATTED OUTPUT USING %
# ============================================================

x = 10
y = 15

print("Value = %d" % x)
print("x = %d, y = %d" % (x, y))

# OUTPUT:
# Value = 10
# x = 10, y = 15

# ============================================================
# 11. STRING FORMATTING
# ============================================================

name = "Linda"

print("Hai %s" % name)
print("Hai (%20s)" % name)
print("Hai (%-20s)" % name)

# OUTPUT:
# Hai Linda
# Hai (               Linda)
# Hai (Linda               )

# ============================================================
# 12. FLOAT FORMATTING
# ============================================================

num = 123.456789

print("The value is: %f" % num)
print("The value is: %.2f" % num)
print("The value is: %.3f" % num)

# OUTPUT:
# The value is: 123.456789
# The value is: 123.46
# The value is: 123.457

# ============================================================
# 13. format() METHOD
# ============================================================

n1 = 1
n2 = 2
n3 = 3

print(
    "number1={0}, number2={1}, number3={2}".format(
        n1, n2, n3
    )
)

# OUTPUT:
# number1=1, number2=2, number3=3

# ============================================================
# 14. NAMED REPLACEMENT FIELDS
# ============================================================

print(
    "number1={two}, number2={one}, number3={three}".format(
        one=1,
        two=2,
        three=3
    )
)

# OUTPUT:
# number1=2, number2=1, number3=3

# ============================================================
# 15. SALARY FORMATTING
# ============================================================

name = "Ravi"
salary = 12500.75

print(
    "Hello %s, your salary is %.2f" %
    (name, salary)
)

# OUTPUT:
# Hello Ravi, your salary is 12500.75

Input Programs

For input programs, show the sample input and output:

# ============================================================
# 16. INPUT STATEMENT
# ============================================================

name = input("Enter your name: ")
print("You entered:", name)

# SAMPLE INPUT:
# Enter your name: Raj

# OUTPUT:
# You entered: Raj

# ============================================================
# 17. ACCEPTING AN INTEGER
# ============================================================

number = int(input("Enter an integer: "))
print("You entered:", number)

# SAMPLE INPUT:
# Enter an integer: 125

# OUTPUT:
# You entered: 125

# ============================================================
# 18. ACCEPTING A FLOAT
# ============================================================

number = float(input("Enter a float number: "))
print("You entered:", number)

# SAMPLE INPUT:
# Enter a float number: 12.345

# OUTPUT:
# You entered: 12.345

# ============================================================
# 19. ACCEPTING TWO NUMBERS
# ============================================================

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("You entered:", x, y)

# SAMPLE INPUT:
# Enter first number: 12
# Enter second number: 45

# OUTPUT:
# You entered: 12 45

# ============================================================
# 20. SUM OF TWO NUMBERS
# ============================================================

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(
    "The sum of {} and {} is {}".format(
        x, y, x + y
    )
)

# SAMPLE INPUT:
# Enter first number: 88
# Enter second number: 98

# OUTPUT:
# The sum of 88 and 98 is 186

# ============================================================
# 21. SUM AND PRODUCT
# ============================================================

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("The sum is:", x + y)
print("The product is:", x * y)

# SAMPLE INPUT:
# Enter first number: 45
# Enter second number: 65

# OUTPUT:
# The sum is: 110
# The product is: 2925

# ============================================================
# 22. MULTIPLE INPUTS IN ONE LINE
# ============================================================

a, b = [int(x) for x in input(
    "Enter two numbers: "
).split()]

print("Sum =", a + b)

# SAMPLE INPUT:
# Enter two numbers: 10 20

# OUTPUT:
# Sum = 30

# ============================================================
# 23. THREE NUMBERS
# ============================================================

a, b, c = [
    int(x)
    for x in input("Enter three numbers: ").split()
]

print("Sum =", a + b + c)

# SAMPLE INPUT:
# Enter three numbers: 10 20 30

# OUTPUT:
# Sum = 60

# ============================================================
# 24. COMMA-SEPARATED INPUT
# ============================================================

a, b, c = [
    int(x)
    for x in input(
        "Enter three numbers: "
    ).split(",")
]

print("Sum =", a + b + c)

# SAMPLE INPUT:
# Enter three numbers: 10,20,30

# OUTPUT:
# Sum = 60

# ============================================================
# 25. GROUP OF STRINGS
# ============================================================

lst = [
    x
    for x in input(
        "Enter strings: "
    ).split(",")
]

print("You entered:", lst)

# SAMPLE INPUT:
# Enter strings: Anil,Vijay,Priya

# OUTPUT:
# You entered: ['Anil', 'Vijay', 'Priya']

eval() Examples

# ============================================================
# 26. eval() FUNCTION
# ============================================================

a = 5
b = 10

result = eval("a + b - 4")

print("Result =", result)

# OUTPUT:
# Result = 11

# ============================================================
# 27. eval() WITH input()
# ============================================================

expression = input("Enter an expression: ")
result = eval(expression)

print("Result =", result)

# SAMPLE INPUT:
# Enter an expression: 10 + 5

# OUTPUT:
# Result = 15

# ============================================================
# 28. ACCEPTING A LIST
# ============================================================

lst = eval(input("Enter a list: "))

print("List:", lst)

# SAMPLE INPUT:
# Enter a list: [10, 20, 30]

# OUTPUT:
# List: [10, 20, 30]

Command-Line Arguments

# ============================================================
# 29. COMMAND LINE ARGUMENTS
# ============================================================

import sys

print("Arguments:", sys.argv)
print("Number of arguments:", len(sys.argv))

# RUN:
# python cmd.py 10 20

# OUTPUT:
# Arguments: ['cmd.py', '10', '20']
# Number of arguments: 3

# ============================================================
# 30. ADD TWO NUMBERS USING COMMAND LINE
# ============================================================

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

print("Sum =", x + y)

# RUN:
# python add.py 10 22

# OUTPUT:
# Sum = 32

# ============================================================
# 31. SUM OF EVEN NUMBERS
# ============================================================

import sys

args = sys.argv[1:]

total = 0

for argument in args:
    number = int(argument)

    if number % 2 == 0:
        total += number

print("Sum of even numbers =", total)

# RUN:
# python even_sum.py 6 8 9 10 11

# OUTPUT:
# Sum of even numbers = 24

argparse Examples

# ============================================================
# 32. ARGPARSE - SQUARE OF A NUMBER
# ============================================================

import argparse

parser = argparse.ArgumentParser(
    description="Find the square of a number"
)

parser.add_argument(
    "num",
    type=int,
    help="Enter an integer number"
)

args = parser.parse_args()

result = args.num ** 2

print("Square value =", result)

# RUN:
# python square.py 5

# OUTPUT:
# Square value = 25

# ============================================================
# 33. ARGPARSE - TWO NUMBERS
# ============================================================

import argparse

parser = argparse.ArgumentParser(
    description="Calculate the sum of two numbers"
)

parser.add_argument("n1", type=float)
parser.add_argument("n2", type=float)

args = parser.parse_args()

result = args.n1 + args.n2

print("Sum =", result)

# RUN:
# python args_sum.py 10.5 15

# OUTPUT:
# Sum = 25.5

# ============================================================
# 34. ARGPARSE - nargs=2
# ============================================================

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("nums", nargs=2)

args = parser.parse_args()

result = float(args.nums[0]) ** float(args.nums[1])

print("Number =", args.nums[0])
print("Power =", args.nums[1])
print("Result =", result)

# RUN:
# python power.py 10.5 3

# OUTPUT:
# Number = 10.5
# Power = 3
# Result = 1157.625

# ============================================================
# 35. ARGPARSE - nargs="+"
# ============================================================

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("nums", nargs="+")

args = parser.parse_args()

for value in args.nums:
    print(value)

# RUN:
# python arguments.py 10 Prasad 78.5

# OUTPUT:
# 10
# Prasad
# 78.5

Follow This:
Concept → Code → Sample Input → Output → Short comment

It makes the file useful both for revision and practical execution, instead of being just a collection of code.
