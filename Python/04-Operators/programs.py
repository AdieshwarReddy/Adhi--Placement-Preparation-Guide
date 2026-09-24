
# ============================================================
# CHAPTER 4 - OPERATORS IN PYTHON
# ============================================================
# Topics:
# 1. Arithmetic Operators
# 2. Operator Precedence
# 3. Assignment Operators
# 4. Unary Minus Operator
# 5. Relational Operators
# 6. Logical Operators
# 7. Boolean Operators
# 8. Bitwise Operators
# 9. Membership Operators
# 10. Identity Operators
# 11. id() Function
# 12. Math Module
# 13. Area of a Circle
# ============================================================


# ------------------------------------------------------------
# 1. Arithmetic Operators
# ------------------------------------------------------------

a = 13
b = 5

print("----- Arithmetic Operators -----")
print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)
print("Division       :", a / b)
print("Modulus        :", a % b)
print("Exponent       :", a ** b)
print("Floor Division :", a // b)


# ------------------------------------------------------------
# 2. Operator Precedence
# ------------------------------------------------------------

print("\n----- Operator Precedence -----")

x = 1
y = 2
z = 3
p = 2
q = 2
c = 3

d = (x + y) * z ** p // q + c

print("Result =", d)


# ------------------------------------------------------------
# 3. Assignment Operators
# ------------------------------------------------------------

print("\n----- Assignment Operators -----")

x = 20
print("Initial x =", x)

x += 10
print("After x += 10 :", x)

x -= 5
print("After x -= 5  :", x)

x *= 2
print("After x *= 2  :", x)

x /= 5
print("After x /= 5  :", x)

x //= 2
print("After x //= 2 :", x)

x %= 3
print("After x %= 3  :", x)

x **= 2
print("After x **= 2 :", x)


# ------------------------------------------------------------
# 4. Unary Minus Operator
# ------------------------------------------------------------

print("\n----- Unary Minus Operator -----")

a = 10

print("a  =", a)
print("-a =", -a)


# ------------------------------------------------------------
# 5. Relational Operators
# ------------------------------------------------------------

print("\n----- Relational Operators -----")

a = 10
b = 20

print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)
print("a == b :", a == b)
print("a != b :", a != b)


# ------------------------------------------------------------
# 6. Relational Operators with if-else
# ------------------------------------------------------------

print("\n----- Relational Operator with if-else -----")

a = 1
b = 2

if a > b:
    print("Yes")
else:
    print("No")


# ------------------------------------------------------------
# 7. Chained Relational Operators
# ------------------------------------------------------------

print("\n----- Chained Relational Operators -----")

x = 15

print("10 < x < 20 :", 10 < x < 20)
print("10 >= x < 20:", 10 >= x < 20)
print("10 < x > 20 :", 10 < x > 20)

print("1 < 2 < 3 < 4 :", 1 < 2 < 3 < 4)
print("1 < 2 > 3 < 4 :", 1 < 2 > 3 < 4)
print("4 > 2 >= 2 > 1:", 4 > 2 >= 2 > 1)


# ------------------------------------------------------------
# 8. Logical Operators
# ------------------------------------------------------------

print("\n----- Logical Operators -----")

x = 1
y = 2

print("x and y :", x and y)
print("x or y  :", x or y)
print("not x   :", not x)


# ------------------------------------------------------------
# 9. Boolean Operators
# ------------------------------------------------------------

print("\n----- Boolean Operators -----")

a = True
b = False

print("a and a :", a and a)
print("a and b :", a and b)
print("a or a  :", a or a)
print("a or b  :", a or b)
print("b or b  :", b or b)
print("not a   :", not a)
print("not b   :", not b)


# ------------------------------------------------------------
# 10. Bitwise Operators
# ------------------------------------------------------------

print("\n----- Bitwise Operators -----")

x = 10
y = 11

print("x & y   :", x & y)
print("x | y   :", x | y)
print("x ^ y   :", x ^ y)
print("~x      :", ~x)
print("x << 2  :", x << 2)
print("x >> 2  :", x >> 2)


# ------------------------------------------------------------
# 11. Decimal to Binary
# ------------------------------------------------------------

print("\n----- Decimal to Binary -----")

number = 45

print("Decimal :", number)
print("Binary  :", bin(number))


# ------------------------------------------------------------
# 12. Binary to Decimal
# ------------------------------------------------------------

print("\n----- Binary to Decimal -----")

binary = "00101101"

decimal = int(binary, 2)

print("Binary  :", binary)
print("Decimal :", decimal)


# ------------------------------------------------------------
# 13. Membership Operators
# ------------------------------------------------------------

print("\n----- Membership Operators -----")

names = ["Rani", "Yamini", "Sushmita", "Veena"]

print("'Rani' in names       :", "Rani" in names)
print("'Rahul' in names      :", "Rahul" in names)
print("'Rahul' not in names :", "Rahul" not in names)


# ------------------------------------------------------------
# 14. Membership Operator with for Loop
# ------------------------------------------------------------

print("\n----- Membership Operator with for Loop -----")

for name in names:
    print(name)


# ------------------------------------------------------------
# 15. Membership Operator with Dictionary
# ------------------------------------------------------------

print("\n----- Membership Operator with Dictionary -----")

postal = {
    "Delhi": 110001,
    "Chennai": 600001,
    "Kolkata": 700001,
    "Bangalore": 560001
}

print("'Delhi' in postal       :", "Delhi" in postal)
print("'Mumbai' in postal      :", "Mumbai" in postal)
print("'Mumbai' not in postal  :", "Mumbai" not in postal)


# ------------------------------------------------------------
# 16. Identity Operators
# ------------------------------------------------------------

print("\n----- Identity Operators -----")

one = [1, 2, 3, 4]
two = [1, 2, 3, 4]

print("one == two :", one == two)
print("one is two :", one is two)


# ------------------------------------------------------------
# 17. Same Object Using Identity Operator
# ------------------------------------------------------------

print("\n----- Same Object -----")

one = [1, 2, 3, 4]
two = one

print("one == two :", one == two)
print("one is two :", one is two)


# ------------------------------------------------------------
# 18. id() Function
# ------------------------------------------------------------

print("\n----- id() Function -----")

one = [1, 2, 3, 4]
two = [1, 2, 3, 4]

print("ID of one :", id(one))
print("ID of two :", id(two))

print("one is two:", one is two)


# ------------------------------------------------------------
# 19. Math Module
# ------------------------------------------------------------

print("\n----- Math Module -----")

import math

print("sqrt(49)      :", math.sqrt(49))
print("pow(5, 3)     :", math.pow(5, 3))
print("factorial(5)  :", math.factorial(5))
print("ceil(4.5)     :", math.ceil(4.5))
print("floor(4.5)    :", math.floor(4.5))
print("fabs(-4.56)   :", math.fabs(-4.56))
print("gcd(25, 30)   :", math.gcd(25, 30))
print("trunc(15.5676):", math.trunc(15.5676))


# ------------------------------------------------------------
# 20. Math Constants
# ------------------------------------------------------------

print("\n----- Math Constants -----")

print("Pi        :", math.pi)
print("Euler's e :", math.e)
print("Infinity  :", math.inf)
print("NaN       :", math.nan)


# ------------------------------------------------------------
# 21. Different Ways to Import a Module
# ------------------------------------------------------------

print("\n----- Different Import Methods -----")

# Method 1:
import math

print("Method 1 - sqrt:", math.sqrt(25))

# Method 2:
import math as m

print("Method 2 - sqrt:", m.sqrt(25))

# Method 3:
from math import sqrt, factorial

print("Method 3 - sqrt     :", sqrt(25))
print("Method 3 - factorial:", factorial(5))


# ------------------------------------------------------------
# 22. Area of a Circle
# ------------------------------------------------------------

print("\n----- Area of Circle -----")

r = 15.5

area = math.pi * r ** 2

print("Radius =", r)
print("Area of circle =", area)


# ============================================================
# END OF CHAPTER 4
# ============================================================

