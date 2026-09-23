
📚 Python — Points to Remember

1. Introduction to Python

Python was developed by Guido van Rossum in 1991.

Python is a high-level programming language.

Python supports functional programming and object-oriented programming concepts.


2. Object-Oriented Concepts

An object represents a physical entity.

The behavior of an object is represented through:

Attributes/Properties → Variables

Actions → Functions/Methods


A class is an abstract idea or blueprint representing the common behavior of objects.

A class does not physically exist until its objects are created.

A group of objects having the same behavior belongs to the same class.


3. Python Compiler

The standard Python implementation is written in C.

It is therefore called CPython.

Other Python implementations include:

Jython

IronPython

PyPy



4. Python Program Execution

The basic execution flow is:

Python Source Code → Python Compiler → Byte Code → PVM → Machine-Level Execution → Output

A Python program is first converted into bytecode.

The bytecode is executed by the Python Virtual Machine (PVM).

Bytecode consists of instructions used to represent Python operations.


5. Python Virtual Machine (PVM)

PVM is the software component responsible for executing Python bytecode.

PVM is commonly referred to as the Python interpreter.

The standard Python implementation primarily uses an interpreter to execute bytecode.

PyPy additionally uses a JIT (Just-In-Time) compiler to improve execution speed.


6. Memory Management

Python programmers generally do not manually allocate or deallocate memory.

Python automatically manages memory.

The Memory Manager allocates memory for objects.

The Garbage Collector releases memory occupied by objects that are no longer needed.

Garbage collection normally happens automatically.

The programmer can also explicitly trigger garbage collection when required.


7. Frozen Binaries

Frozen binaries are executable packages containing Python programs together with the required Python runtime/compiler components and libraries.

They allow Python applications to be distributed and executed without requiring a separate Python installation in some deployment setups.


8. py_compile Module

The py_compile module can compile a Python source file into a .pyc file.

A .pyc file contains Python bytecode instructions.


Example:

import py_compile

py_compile.compile("program.py")

9. dis Module

The dis module is used to display Python bytecode in a human-readable form.

It is useful for understanding how Python instructions are translated into bytecode.


Example:

import dis

dis.dis(my_function)

⭐ Quick Revision

Python
   ↓
Source Code
   ↓
Compiler
   ↓
Bytecode
   ↓
PVM / Python Interpreter
   ↓
Execution
   ↓
Output

Important Terms

Term	Meaning

Python	High-level programming language
Guido van Rossum	Creator of Python
CPython	Standard Python implementation written in C
Bytecode	Intermediate instructions generated from Python code
PVM	Executes Python bytecode
JIT	Just-In-Time compiler used by PyPy
Memory Manager	Allocates memory for objects
Garbage Collector	Frees unused object memory
.pyc	File containing Python bytecode
py_compile	Compiles Python source to bytecode
dis	Displays bytecode in human-readable form
Frozen Binary	Distributable executable Python application package
