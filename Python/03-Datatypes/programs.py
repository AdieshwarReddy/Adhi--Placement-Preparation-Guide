# ============================================================
# UNIT 3 - PYTHON PROGRAMS
# Variables, Comments, Datatypes, Type Conversion,
# Strings, Lists, Tuples, Sets, Dictionaries and Identifiers
# ============================================================


# ------------------------------------------------------------
# 1. PROGRAM TO ADD TWO NUMBERS
# ------------------------------------------------------------

a = 10
b = 15
c = a + b

print("Sum =", c)

# Output:
# Sum = 25


# ------------------------------------------------------------
# 2. SINGLE-LINE COMMENT
# ------------------------------------------------------------

# This is a single-line comment
a = 10

print(a)

# Output:
# 10


# ------------------------------------------------------------
# 3. MULTI-LINE COMMENT
# ------------------------------------------------------------

"""
This is a multi-line comment.
It can contain multiple lines.
"""

print("Python")

# Output:
# Python


# ------------------------------------------------------------
# 4. FUNCTION WITH TWO FUNCTIONS
# ------------------------------------------------------------

def add(x, y):
    """This function finds the sum of two numbers."""
    print("Sum =", x + y)


def message():
    """This function displays a welcome message."""
    print("Welcome to Python")


add(10, 25)
message()

# Output:
# Sum = 35
# Welcome to Python


# ------------------------------------------------------------
# 5. TYPE OF VARIABLE
# ------------------------------------------------------------

a = 10
print(type(a))

# Output:
# <class 'int'>


# ------------------------------------------------------------
# 6. SUM OF TWO COMPLEX NUMBERS
# ------------------------------------------------------------

c1 = 2.5 + 2.5j
c2 = 3.0 - 0.5j
c3 = c1 + c2

print("Sum =", c3)

# Output:
# Sum = (5.5+2j)


# ------------------------------------------------------------
# 7. INTEGER TYPE CONVERSION
# ------------------------------------------------------------

x = 15.56

print(int(x))

# Output:
# 15


# ------------------------------------------------------------
# 8. FLOAT TYPE CONVERSION
# ------------------------------------------------------------

num = 15

print(float(num))

# Output:
# 15.0


# ------------------------------------------------------------
# 9. CONVERT INTEGER TO COMPLEX NUMBER
# ------------------------------------------------------------

n = 10

print(complex(n))

# Output:
# (10+0j)


# ------------------------------------------------------------
# 10. CREATE COMPLEX NUMBER USING REAL AND IMAGINARY PART
# ------------------------------------------------------------

a = 10
b = -5

print(complex(a, b))

# Output:
# (10-5j)


# ------------------------------------------------------------
# 11. CONVERT OCTAL, BINARY AND HEXADECIMAL TO DECIMAL
# ------------------------------------------------------------

n1 = "17"
n2 = "1110010"
n3 = "1c2"

print("Octal 17 =", int(n1, 8))
print("Binary 1110010 =", int(n2, 2))
print("Hexadecimal 1c2 =", int(n3, 16))

# Output:
# Octal 17 = 15
# Binary 1110010 = 114
# Hexadecimal 1c2 = 450


# ------------------------------------------------------------
# 12. CONVERT DECIMAL TO BINARY, OCTAL AND HEXADECIMAL
# ------------------------------------------------------------

a = 10

print(bin(a))
print(oct(a))
print(hex(a))

# Output:
# 0b1010
# 0o12
# 0xa


# ------------------------------------------------------------
# 13. BOOLEAN DATATYPE
# ------------------------------------------------------------

a = 10
b = 20

print(a < b)
print(a > b)

# Output:
# True
# False


# ------------------------------------------------------------
# 14. BOOLEAN VALUES IN ARITHMETIC
# ------------------------------------------------------------

print(True + True)
print(True - False)

# Output:
# 2
# 1


# ------------------------------------------------------------
# 15. BOOLEAN WITH IF CONDITION
# ------------------------------------------------------------

a = 10
b = 20

if a < b:
    print("Hello")

# Output:
# Hello


# ------------------------------------------------------------
# 16. BOOLEAN VARIABLES
# ------------------------------------------------------------

a = 10 > 5
print(a)

a = 5 >= 10
print(a)

# Output:
# True
# False


# ------------------------------------------------------------
# 17. STRING DATATYPE
# ------------------------------------------------------------

s = "Welcome to Python"

print(s)

# Output:
# Welcome to Python


# ------------------------------------------------------------
# 18. STRING INDEXING
# ------------------------------------------------------------

s = "Welcome to Core Python"

print(s[0])

# Output:
# W


# ------------------------------------------------------------
# 19. STRING SLICING
# ------------------------------------------------------------

s = "Welcome to Core Python"

print(s[3:7])
print(s[11:])
print(s[-1])

# Output:
# come
# Core Python
# n


# ------------------------------------------------------------
# 20. STRING REPETITION
# ------------------------------------------------------------

s = "Welcome to Core Python"

print(s * 2)

# Output:
# Welcome to Core PythonWelcome to Core Python


# ------------------------------------------------------------
# 21. MULTI-LINE STRING
# ------------------------------------------------------------

s = """This is a
multi-line
string."""

print(s)

# Output:
# This is a
# multi-line
# string.


# ------------------------------------------------------------
# 22. STRING CONTAINING SINGLE QUOTES
# ------------------------------------------------------------

s = """This is 'Core Python' book."""

print(s)

# Output:
# This is 'Core Python' book.


# ------------------------------------------------------------
# 23. STRING CONTAINING DOUBLE QUOTES
# ------------------------------------------------------------

s = '''This is "Core Python" book.'''

print(s)

# Output:
# This is "Core Python" book.


# ------------------------------------------------------------
# 24. STRING WITH NEW LINE ESCAPE CHARACTER
# ------------------------------------------------------------

s = "This is\nPython"

print(s)

# Output:
# This is
# Python


# ------------------------------------------------------------
# 25. BYTES DATATYPE
# ------------------------------------------------------------

elements = [10, 20, 0, 40, 15]

x = bytes(elements)

for i in x:
    print(i)

# Output:
# 10
# 20
# 0
# 40
# 15


# ------------------------------------------------------------
# 26. BYTEARRAY DATATYPE
# ------------------------------------------------------------

elements = [10, 20, 0, 40, 15]

x = bytearray(elements)

print(x[0])

# Modify first element
x[0] = 99

for i in x:
    print(i)

# Output:
# 10
# 99
# 20
# 0
# 40
# 15


# ------------------------------------------------------------
# 27. LIST WITH DIFFERENT TYPES OF ELEMENTS
# ------------------------------------------------------------

lst = [10, 20, 15.5, "Vijay", "Mary"]

print(lst)

# Output:
# [10, 20, 15.5, 'Vijay', 'Mary']


# ------------------------------------------------------------
# 28. LIST INDEXING
# ------------------------------------------------------------

lst = [10, 20, 15.5, "Vijay", "Mary"]

print(lst[0])
print(lst[-1])

# Output:
# 10
# Mary


# ------------------------------------------------------------
# 29. LIST SLICING
# ------------------------------------------------------------

lst = [10, 20, 15.5, "Vijay", "Mary"]

print(lst[1:3])

# Output:
# [20, 15.5]


# ------------------------------------------------------------
# 30. LIST REPETITION
# ------------------------------------------------------------

lst = [10, 20, 15.5, "Vijay", "Mary"]

print(lst * 2)

# Output:
# [10, 20, 15.5, 'Vijay', 'Mary',
#  10, 20, 15.5, 'Vijay', 'Mary']


# ------------------------------------------------------------
# 31. TUPLE
# ------------------------------------------------------------

tpl = (10, 20, 15.5, "Vijay", "Mary")

print(tpl)
print(tpl[0])
print(tpl[1:3])
print(tpl[-2])

# Output:
# (10, 20, 15.5, 'Vijay', 'Mary')
# 10
# (20, 15.5)
# Vijay


# ------------------------------------------------------------
# 32. RANGE DATATYPE
# ------------------------------------------------------------

r = range(10)

for i in r:
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


# ------------------------------------------------------------
# 33. RANGE WITH START, STOP AND STEP
# ------------------------------------------------------------

r = range(30, 40, 2)

for i in r:
    print(i)

# Output:
# 30
# 32
# 34
# 36
# 38


# ------------------------------------------------------------
# 34. CONVERT RANGE INTO LIST
# ------------------------------------------------------------

lst = list(range(10))

print(lst)

# Output:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# ------------------------------------------------------------
# 35. SET
# ------------------------------------------------------------

s = {10, 20, 30, 20, 50}

print(s)

# Output:
# Duplicate 20 is removed.
# Order may be different.


# ------------------------------------------------------------
# 36. CREATE SET FROM STRING
# ------------------------------------------------------------

ch = set("Hello")

print(ch)

# Output:
# Duplicate characters are removed.
# Order may be different.


# ------------------------------------------------------------
# 37. CONVERT LIST INTO SET
# ------------------------------------------------------------

lst = [1, 2, 5, 4, 3]

s = set(lst)

print(s)

# Output:
# {1, 2, 3, 4, 5}


# ------------------------------------------------------------
# 38. ADD ELEMENTS TO SET USING update()
# ------------------------------------------------------------

s = {1, 2, 3, 4, 5}

s.update([50, 60])

print(s)

# Output:
# {1, 2, 3, 4, 5, 50, 60}


# ------------------------------------------------------------
# 39. REMOVE ELEMENT FROM SET
# ------------------------------------------------------------

s = {1, 2, 3, 4, 5, 50, 60}

s.remove(50)

print(s)

# Output:
# {1, 2, 3, 4, 5, 60}


# ------------------------------------------------------------
# 40. FROZENSET
# ------------------------------------------------------------

s = {50, 60, 70, 80, 90}

fs = frozenset(s)

print(fs)

# Output:
# frozenset({...})


# ------------------------------------------------------------
# 41. FROZENSET FROM STRING
# ------------------------------------------------------------

fs = frozenset("abcdefg")

print(fs)

# Output:
# frozenset({...})


# ------------------------------------------------------------
# 42. DICTIONARY
# ------------------------------------------------------------

d = {
    10: "Kamal",
    11: "Pranav",
    12: "Hasini",
    13: "Anup",
    14: "Reethu"
}

print(d)

# Output:
# {10: 'Kamal', 11: 'Pranav', 12: 'Hasini',
#  13: 'Anup', 14: 'Reethu'}


# ------------------------------------------------------------
# 43. ACCESS DICTIONARY VALUE USING KEY
# ------------------------------------------------------------

d = {
    10: "Kamal",
    11: "Pranav",
    12: "Hasini"
}

print(d[11])

# Output:
# Pranav


# ------------------------------------------------------------
# 44. DICTIONARY KEYS
# ------------------------------------------------------------

d = {
    10: "Kamal",
    11: "Pranav",
    12: "Hasini"
}

print(d.keys())

# Output:
# dict_keys([10, 11, 12])


# ------------------------------------------------------------
# 45. DICTIONARY VALUES
# ------------------------------------------------------------

d = {
    10: "Kamal",
    11: "Pranav",
    12: "Hasini"
}

print(d.values())

# Output:
# dict_values(['Kamal', 'Pranav', 'Hasini'])


# ------------------------------------------------------------
# 46. UPDATE DICTIONARY VALUE
# ------------------------------------------------------------

d = {
    10: "Kamal",
    11: "Pranav",
    12: "Hasini"
}

d[10] = "Hareesh"

print(d)

# Output:
# {10: 'Hareesh', 11: 'Pranav', 12: 'Hasini'}


# ------------------------------------------------------------
# 47. DELETE DICTIONARY ELEMENT
# ------------------------------------------------------------

d = {
    10: "Kamal",
    11: "Pranav",
    12: "Hasini"
}

del d[11]

print(d)

# Output:
# {10: 'Kamal', 12: 'Hasini'}


# ------------------------------------------------------------
# 48. EMPTY DICTIONARY
# ------------------------------------------------------------

d = {}

d[10] = "Kamal"
d[11] = "Pranav"

print(d)

# Output:
# {10: 'Kamal', 11: 'Pranav'}


# ------------------------------------------------------------
# 49. CHECK DATATYPE USING type()
# ------------------------------------------------------------

a = 15
b = 15.5
c = "Python"
d = [1, 2, 3]
e = (1, 2, 3)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Output:
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>


# ------------------------------------------------------------
# 50. CHARACTER IN PYTHON
# ------------------------------------------------------------

ch = 'A'

print(type(ch))

# Output:
# <class 'str'>


# ------------------------------------------------------------
# 51. ACCESS INDIVIDUAL CHARACTERS FROM STRING
# ------------------------------------------------------------

s = "Bharat"

print(s[0])
print(s[1])
print(s[2])

# Output:
# B
# h
# a


# ------------------------------------------------------------
# 52. DISPLAY ALL CHARACTERS USING FOR LOOP
# ------------------------------------------------------------

s = "Bharat"

for i in s:
    print(i)

# Output:
# B
# h
# a
# r
# a
# t


# ------------------------------------------------------------
# 53. CHECK WHETHER CHARACTER IS UPPERCASE
# ------------------------------------------------------------

s = "Bharat"

print(s[0].isupper())
print(s[1].isupper())

# Output:
# True
# False


# ============================================================
# QUICK BULLET POINTS
# ============================================================

# 1. Python converts source code into bytecode.
# 2. PVM executes the bytecode.
# 3. Comments are non-executable statements.
# 4. '#' is used for single-line comments.
# 5. Triple quotes can be used for multi-line strings/comments.
# 6. A docstring documents a function, class or method.
# 7. Python variables do not require explicit datatype declaration.
# 8. Python determines the datatype from the value assigned.
# 9. int() converts a value to integer.
# 10. float() converts a value to float.
# 11. complex() creates a complex number.
# 12. bin() converts a number to binary representation.
# 13. oct() converts a number to octal representation.
# 14. hex() converts a number to hexadecimal representation.
# 15. bool represents True or False.
# 16. Strings are indexed starting from 0.
# 17. Strings support indexing and slicing.
# 18. bytes cannot be modified.
# 19. bytearray can be modified.
# 20. Lists can contain different types of elements.
# 21. Tuples cannot be modified.
# 22. range represents a sequence of numbers.
# 23. Sets are unordered and do not allow duplicates.
# 24. frozenset cannot be modified.
# 25. Dictionaries store key-value pairs.
# 26. type() is used to find the datatype.
# 27. Python has no separate char datatype.
# 28. A single character is treated as a string.
# 29. Python is case-sensitive.
# 30. Identifiers can contain letters, digits and underscore.
# 31. An identifier should not start with a number.
# 32. Special symbols such as #, $, %, @ are not allowed in identifiers.
# 33. Reserved words cannot be used as identifiers.
# 34. Constants are conventionally written in CAPITAL LETTERS.
# 35. Python does not have a special keyword for declaring constants.
