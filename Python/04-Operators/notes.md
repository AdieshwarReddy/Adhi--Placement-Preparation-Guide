📘 Chapter 4 — Operators in Python

Table of Contents

1. Operators and Operands


2. Arithmetic Operators


3. Python Interpreter as a Calculator


4. Assignment Operators


5. Unary Minus Operator


6. Relational Operators


7. Logical Operators


8. Boolean Operators


9. Bitwise Operators


10. Membership Operators


11. Identity Operators


12. id() Function


13. Modules in Python


14. math Module


15. Different Ways to Import a Module


16. Points to Remember




---

1. Operators and Operands

An operator is a symbol that performs an operation.

An operand is the value or variable on which an operator acts.


Example:

a + b

Here:

+ → Operator

a, b → Operands



---

2. Arithmetic Operators

Arithmetic operators are used to perform mathematical calculations.

Operator	Operation	Example	Result

+	Addition	10 + 5	15
-	Subtraction	10 - 5	5
*	Multiplication	10 * 5	50
/	Division	10 / 5	2.0
//	Floor Division	10 // 3	3
%	Modulus	10 % 3	1
**	Exponentiation	2 ** 3	8


Example

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)


---

3. Python Interpreter as a Calculator

Python interpreter can be directly used as a calculator.

>>> 10 + 20
30

>>> 10 * 5
50

>>> 20 / 4
5.0

>>> 2 ** 3
8

This is useful for quickly performing calculations.


---

4. Assignment Operators

Assignment operators are used to assign or update values of variables.

Operator	Example	Meaning

=	a = 10	Assign 10 to a
+=	a += 5	a = a + 5
-=	a -= 5	a = a - 5
*=	a *= 5	a = a * 5
/=	a /= 5	a = a / 5
//=	a //= 5	a = a // 5
%=	a %= 5	a = a % 5
**=	a **= 5	a = a ** 5


Example

a = 10
a += 5

print(a)

Output:

15


---

5. Unary Minus Operator

The unary minus operator - is used to negate a value.

a = 10
print(-a)

Output:

-10

It changes a positive value to negative and a negative value to positive.


---

6. Relational Operators

Relational operators are used to compare two values.

The result is either:

True

or

False

Operator	Meaning	Example

>	Greater than	10 > 5
<	Less than	10 < 5
>=	Greater than or equal	10 >= 10
<=	Less than or equal	5 <= 10
==	Equal to	10 == 10
!=	Not equal to	10 != 5


Example:

a = 10
b = 20

print(a < b)
print(a == b)

Output:

True
False

Relational operators are commonly used to create conditions.


---

7. Logical Operators

Logical operators are used to combine more than one condition.

and

Returns True when both conditions are True.

age = 20
marks = 80

print(age >= 18 and marks >= 50)

Output:

True

or

Returns True when at least one condition is True.

age = 20
marks = 40

print(age >= 18 or marks >= 50)

Output:

True

not

Reverses the result.

a = True
print(not a)

Output:

False

genui{"learning_viz":{"type_id":"BOOLEAN_LOGIC","initial_values":{"inputA":true,"inputB":false,"operator":"and"}}}
---

8. Boolean Operators

Boolean operators work with Boolean values:

True
False

They produce a Boolean result.

Example:

a = True
b = False

print(a and b)
print(a or b)
print(not a)

Output:

False
True
False


---

9. Bitwise Operators

Bitwise operators work on the individual bits (0 and 1) of numbers.

Operator	Name

&	Bitwise AND
`	`
^	Bitwise XOR
~	Bitwise NOT
<<	Left Shift
>>	Right Shift


Example:

a = 5
b = 3

print(a & b)

Binary representation:

5 = 101
3 = 011
---------
    001

Therefore:

Output: 1


---

10. Membership Operators

Membership operators are used to check whether an element exists in a sequence.

Two membership operators are:

in

not in


in

numbers = [10, 20, 30]

print(20 in numbers)

Output:

True

not in

print(50 not in numbers)

Output:

True

They can be used with strings, lists, tuples, sets, etc.


---

11. Identity Operators

Identity operators compare the identity/memory location of objects.

There are two identity operators:

is

is not


Example:

a = [10, 20]
b = a

print(a is b)

Output:

True

a and b refer to the same object.

Important

Identity operators are different from equality operators.

==   → compares values
is   → compares object identity


---

12. id() Function

The id() function returns the identification number associated with an object.

Example:

a = 10

print(id(a))

The exact number can vary between executions.

We can use id() to examine object identity.

a = [1, 2]
b = a

print(id(a))
print(id(b))

Both refer to the same object, so their IDs are the same.


---

13. Modules in Python

A module is a Python file containing useful objects such as:

Functions

Classes

Variables


Modules allow us to reuse code instead of writing everything again.


---

14. math Module

Python provides a module called math.

The math module contains several functions useful for mathematical calculations.

Examples include:

sqrt()
factorial()
ceil()
floor()
pow()

Example:

import math

print(math.sqrt(25))

Output:

5.0


---

15. Different Ways to Import a Module

There are three common ways to import a module.

Method 1: import module

import math

print(math.sqrt(25))


---

Method 2: import module as anothername

We can give the module another name.

import math as m

print(m.sqrt(25))

Here:

math → Original module name
m    → Another name / alias


---

Method 3: from module import object

We can directly import specific objects from a module.

from math import sqrt, factorial

print(sqrt(25))
print(factorial(5))

Here we don't need to write:

math.sqrt()

Instead, we can directly use:

sqrt()


---

📝 Quick Revision

Operator
   ↓
Performs an operation
   ↓
Works on operands

Main Operator Categories

Arithmetic       → +  -  *  /  //  %  **
Assignment       → =  +=  -=  *=  ...
Relational       → >  <  >=  <=  ==  !=
Logical          → and  or  not
Bitwise          → &  |  ^  ~  <<  >>
Membership       → in  not in
Identity         → is  is not

Modules

Module
   ↓
Python file containing reusable objects
   ↓
Functions + Classes + Variables


---

⭐ Points to Remember

1. An operator is a symbol that performs an operation.


2. An operator acts on variables or values called operands.


3. Python's interpreter can be used as a calculator.


4. Arithmetic operators perform mathematical operations.


5. Assignment operators assign or update values.


6. The unary minus operator is used to negate a value.


7. Relational operators compare two quantities and produce True or False.


8. Logical operators combine multiple conditions.


9. Boolean operators work with Boolean values and produce Boolean results.


10. Bitwise operators work on individual bits (0 and 1).


11. Membership operators in and not in check whether an element exists in a sequence.


12. Identity operators is and is not compare the identity of objects.


13. The id() function gives the identification number of an object.


14. A module is a Python file containing reusable functions, classes, and variables.


15. The math module provides functions for mathematical calculations.


16. Modules can be imported using import, import ... as, or from ... import.




---

🎯 One-Minute Exam Revision

Operator → Performs an operation
Operand → Value on which operator acts
Arithmetic → Mathematical calculations
Assignment → Assign/update values
Relational → Compare values
Logical → Combine conditions
Boolean → Works with True/False
Bitwise → Works with bits
Membership → Checks presence
Identity → Checks object identity
id() → Gives object identification number
Module → Reusable Python file
math → Mathematical functions module
