Python Programs — Code & Output

============================================================
PROGRAM 1: Add Two Numbers
============================================================

# Python program to add two numbers

a = 10
b = 10

print("Sum =", (a + b))


OUTPUT:
Sum = 20


============================================================
PROGRAM 2: Compile a Python File into .pyc
============================================================

# compile_program.py

import py_compile

py_compile.compile("first.py")


OUTPUT:
A file named __pycache__/first.cpython-XX.pyc is created.

(Note: XX depends on the Python version.)


============================================================
PROGRAM 3: View Python Bytecode using dis Module
============================================================

# first.py

a = 10
b = 10

print("Sum =", (a + b))


COMMAND:

python -m dis first.py


SAMPLE OUTPUT:

  0 RESUME                   0

  2 LOAD_CONST               0 (10)
  4 STORE_NAME               0 (a)

  6 LOAD_CONST               0 (10)
  8 STORE_NAME               1 (b)

 10 PUSH_NULL
 12 LOAD_NAME                2 (print)
 14 LOAD_CONST               1 ('Sum =')
 16 LOAD_NAME                0 (a)
 18 LOAD_NAME                1 (b)
 20 BINARY_OP                0 (+)
 24 PRECALL                  2
 28 CALL                     2
 38 POP_TOP
 40 LOAD_CONST               2 (None)
 42 RETURN_VALUE


============================================================
PROGRAM 4: Execute the Python Program
============================================================

# first.py

a = 10
b = 10

print("Sum =", (a + b))


COMMAND:

python first.py


OUTPUT:

Sum = 20


============================================================
IMPORTANT FLOW
============================================================

first.py
   ↓
Python Compiler
   ↓
Bytecode
   ↓
.pyc file
   ↓
Python Virtual Machine (PVM)
   ↓
Output

============================================================
IMPORTANT COMMANDS
============================================================

Run Python program:

python first.py

Compile Python file:

python -m py_compile first.py

View bytecode:

python -m dis first.py

============================================================
NOTE
============================================================

The exact bytecode output can change between Python versions.
The example above uses the modern Python bytecode format.
============================================================
