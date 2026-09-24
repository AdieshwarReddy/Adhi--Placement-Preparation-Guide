
📌 Points to Remember — Chapter 5

Python provides the print() function to display output or results.

The print() function can be used with variables, strings, lists, tuples, dictionaries, and other objects.

The format() method can be used with replacement fields to format output.

Python also supports format strings such as %d, %c, %s, and %.2f for formatted output.

Python provides the input() function to accept data from the keyboard.

The input() function always returns the entered value as a string.

We can use int() or float() to convert input strings into integer or floating-point values.


x = int(input("Enter a number: "))
x = float(input("Enter a number: "))

To accept multiple values in the same line, we can use input() with the split() method.


a, b = (int(x) for x in input("Enter two numbers: ").split())

Command-line arguments are values passed to a Python program from the command prompt or terminal.

Command-line arguments are stored in sys.argv as a list.

sys.argv[0] represents the program name.

sys.argv[1] represents the first command-line argument.

sys.argv[2] represents the second command-line argument, and so on.

len(sys.argv) gives the total number of elements in the sys.argv list, including the program name.

To access all command-line arguments except the program name, we can use:


args = sys.argv[1:]

The argparse module is used to create user-friendly command-line argument programs.

The argparse module can automatically generate help messages, usage messages, and error messages when invalid arguments are provided.
