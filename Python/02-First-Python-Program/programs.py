
# ============================================================
# CHAPTER 2: PYTHON PROGRAMS
# ============================================================


# ============================================================
# PROGRAM 1: Add Two Numbers
# ============================================================

# Store two numbers
a = 10
b = 15

# Add the numbers
c = a + b

# Display the result
print("Sum =", c)


# OUTPUT:
# Sum = 25


# ============================================================
# PROGRAM 2: Using Python Comments
# ============================================================

# This is a comment.
# Comments are not executed by Python.

a = 10
b = 20

print("Sum =", a + b)

# OUTPUT:
# Sum = 30


# ============================================================
# PROGRAM 3: Add Two Numbers Using Python Command Line
# ============================================================

# Type the following statements one by one at the >>> prompt:

a = 10
b = 20
c = a + b
print("Sum =", c)

# OUTPUT:
# Sum = 30

# To exit the Python command line:
# exit()


# ============================================================
# PROGRAM 4: Check Python Installation
# ============================================================

print("Python is installed successfully!")

# OUTPUT:
# Python is installed successfully!


# ============================================================
# PROGRAM 5: Import NumPy
# ============================================================

import numpy

print("NumPy is installed successfully!")

# OUTPUT:
# NumPy is installed successfully!


# ============================================================
# PROGRAM 6: Import Pandas
# ============================================================

import pandas

print("Pandas is installed successfully!")

# OUTPUT:
# Pandas is installed successfully!


# ============================================================
# PROGRAM 7: Import Matplotlib
# ============================================================

import matplotlib

print("Matplotlib is installed successfully!")

# OUTPUT:
# Matplotlib is installed successfully!


# ============================================================
# PROGRAM 8: Check Installed Modules
# ============================================================

help("modules")

# OUTPUT:
# Displays the list of Python modules installed
# in the current Python environment.


# ============================================================
# PROGRAM 9: Getting Help in Python
# ============================================================

help(print)

# OUTPUT:
# Displays documentation/help information
# about the print() function.


# ============================================================
# PROGRAM 10: Simple Python Calculation
# ============================================================

a = 10
b = 15

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print("Addition =", addition)
print("Subtraction =", subtraction)
print("Multiplication =", multiplication)
print("Division =", division)

# OUTPUT:
# Addition = 25
# Subtraction = -5
# Multiplication = 150
# Division = 0.6666666666666666


# ============================================================
# PROGRAM 11: Display Python Version
# ============================================================

import sys

print("Python Version:")
print(sys.version)

# OUTPUT:
# Displays the Python version installed on the computer.
# Example:
# Python 3.x.x ...


# ============================================================
# PROGRAM 12: Using exit() and quit()
# ============================================================

# These commands are used to exit the Python interactive shell.

# exit()
# OR
# quit()

# OUTPUT:
# Python interactive shell will be closed.


# ============================================================
# IMPORTANT COMMANDS
# ============================================================

# Check Python version:
# python --version

# Start Python:
# python

# Run a Python program:
# python first.py

# Compile a Python program:
# python -m py_compile first.py

# View bytecode:
# python -m dis first.py

# Install NumPy:
# pip install numpy

# Install Pandas:
# pip install pandas

# Install xlrd:
# pip install xlrd

# Install Matplotlib:
# pip install matplotlib


# ============================================================
# PROGRAM EXECUTION FLOW
# ============================================================

# Python Source Code (.py)
#          ↓
# Python Compiler
#          ↓
# Bytecode
#          ↓
# Python Virtual Machine (PVM)
#          ↓
# Output


# ============================================================
# NOTE
# ============================================================

# The exact package versions shown in older textbooks
# may be different from the versions available today.
#
# Use:
#     pip install numpy
#     pip install pandas
#     pip install matplotlib
#
# to install the current compatible versions.
