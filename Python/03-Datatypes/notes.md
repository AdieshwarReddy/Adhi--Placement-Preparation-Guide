
# Unit 3 — Python Variables, Data Types, Literals & Identifiers

## Points to Remember

### 1. Variable
- A variable represents a **memory location** where some data can be stored.

### 2. Comments
- Python supports **single-line comments** using the hash symbol `#`.
- Example:
  ```python
  # This is a single-line comment

Triple single quotes (''') or triple double quotes (""") can be used for multi-line text/comments.


3. Docstrings

A docstring is a string written inside triple single quotes (''') or triple double quotes (""").

It is written as the first statement inside a function, class, or method.

Docstrings are useful for creating API documentation containing descriptions of the features of a program or software.


Example:

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

4. Datatype

A datatype represents the type of data stored in a variable.

The actual data stored in a variable is called a literal.


Example:

x = 10

Here:

x → Variable

int → Datatype

10 → Literal



---

Built-in Datatypes

Python has four major categories of built-in datatypes:

1. Numeric types


2. Sequences


3. Sets


4. Mappings




---

5. Binary Literal

A binary literal is represented using 0b or 0B at the beginning of a number.


Example:

x = 0b1010


---

6. Octal Literal

An octal literal is represented using 0o or 0O at the beginning of a number.


Example:

x = 0o17


---

7. Hexadecimal Literal

If a number starts with 0x or 0X, it is considered a hexadecimal number.


Example:

x = 0x1A


---

8. Boolean Datatype

The bool datatype represents either:

True

False


True is internally represented as 1.

False is internally represented as 0.


Example:

x = True
y = False


---

9. String Literal

A string literal can be enclosed in:

Single quotes ' '

Double quotes " "


If a string spans multiple lines, it can be enclosed inside:

Triple single quotes ''' '''

Triple double quotes """ """



Example:

name = 'Python'
name = "Python"

message = '''This is
a multi-line
string.'''


---

Sequence Datatypes

10. List

A list is a dynamically growing array that can store different types of elements.

Lists are written using square brackets [ ].

List elements can be modified.


Example:

items = [10, "Python", 20.5]


---

11. Tuple

A tuple is similar to a list.

Its elements cannot be modified after creation.

A tuple uses parentheses ( ).


Example:

items = (10, 20, 30)


---

12. Range

The range datatype represents a sequence of numbers.

It is generally used to repeat a for loop.


Example:

for i in range(5):
    print(i)

Output:

0
1
2
3
4


---

Set Datatypes

13. Set

A set is an unordered collection of elements.

A set uses curly braces { }.


Example:

numbers = {10, 20, 30}


---

14. Frozenset

A frozenset is similar to a set.

Its elements cannot be modified.


Example:

numbers = frozenset([10, 20, 30])


---

Mapping Datatype

15. Dictionary (dict)

A dict represents a group of elements in the form of key-value pairs.

When a key is given, its corresponding value can be obtained.


Example:

student = {
    "name": "Rahul",
    "age": 20
}

Here:

"name" → Key

"Rahul" → Value

"age" → Key

20 → Value



---

16. type() Function

We can use the type() function to determine the datatype of a variable.


Example:

x = 10
print(type(x))

Output:

<class 'int'>


---

17. Single Character Datatype

Python does not have a separate datatype for a single character.

A single character is treated as a string.


Example:

ch = 'A'
print(type(ch))

Output:

<class 'str'>


---

18. Constant

A constant represents a fixed value that should not be changed.

Python does not provide a special datatype or keyword for defining constants.

By convention, constants are written using uppercase letters.


Example:

PI = 3.14
MAX_VALUE = 100


---

19. Identifier

An identifier is a name given to a variable, function, class, etc.


Examples:

name = "Python"     # name is an identifier

def display():      # display is an identifier
    pass


---

20. Naming Conventions

The rules and conventions used for writing names of:

Packages

Modules

Classes

Functions

Variables

etc.



are called naming conventions.

Example:

student_name = "Rahul"


---

🧠 Quick Revision

Topic	Key Point

Variable	Represents a memory location
#	Single-line comment
''' ''' / """ """	Multi-line strings/comments
Docstring	Documentation inside function/class/method
Datatype	Type of data
Literal	Actual value/data
0b / 0B	Binary
0o / 0O	Octal
0x / 0X	Hexadecimal
bool	True or False
String	Sequence of characters
List	Mutable collection using [ ]
Tuple	Immutable collection using ( )
Range	Sequence of numbers
Set	Unordered collection using { }
Frozenset	Immutable set
Dictionary	Key-value pairs
type()	Finds datatype
Character	No separate character datatype in Python
Constant	Fixed value; Python has no special constant keyword
Identifier	Name given to program elements
Naming Convention	Rules for naming program elements
