15-9-2026 


Flowcharts and pseudocodes :

what are flowcharts :
A flowchart is a diagram that visually represents a step-by-step process, workflow, or computer algorithm using connected shapes and arrows.

Common Symbols components :
Oval (Terminator): Marks the start or end point of a process.
Rectangle (Process): Represents a single action, task, or step.
Diamond (Decision): Shows a question or branch point where the path splits based on a "yes/no" or "true/false" condition.
Parallelogram (Input/Output): Indicates data coming in or going out.
Arrows (Flow Line): Connects the shapes to show the direction and sequence of steps

pseudocode:
a simplified, language-agnostic way of writing down your algorithmic logic using plain English combined with basic programming constructs (like loops and conditionals)
Here agnostic means written in plain human-readable text and basic logic structures.

Example 1 : sum of 2 numbers 

pseudocode :
START
DECLARE num1, num2, sum
PRINT "Enter first number:"
INPUT num1
PRINT "Enter second number:"
INPUT num2
sum = num1 + num2
PRINT "The sum is: ", sum
END

Flowchart Steps
A flowchart maps these steps using standard geometric shapes:

* **Start/End:** Draw an **oval** shape labeled `Start` at the top and `End` at the bottom.
* **Input:** Draw a **parallelogram** labeled `Input num1, num2` to get the numbers from the user.
* **Process:** Draw a **rectangle** labeled `sum = num1 + num2` to perform the addition.
* **Output:** Draw a **parallelogram** labeled `Print sum` to show the final result.
* **Flow Lines:** Connect each shape in order using **arrows**.

program:
# Define the two numbers
num1 = 5
num2 = 10
# Calculate the sum
total_sum = num1 + num2
# Display the result
print(f"The sum is: {total_sum}") # here f is the formating string it is not normal string it takes input from the input



Example 2: : print n natural numbers 

# Get the value of N from the user
N = int(input("Enter the value of N: "))

# Loop from 1 to N and print each number
for i in range(1, N + 1):
    # Display the result using an f-string
    print(f"Current natural number: {i}")

pseudo code:

START
DECLARE N, i
PRINT "Enter the value of N:"
INPUT N
i = 1
WHILE i <= N
    PRINT i
    i = i + 1
ENDWHILE
END

Flowchart Steps:

A flowchart maps these steps using standard geometric shapes:
Start/End: Draw an oval shape labeled Start at the top and End at the bottom.
Input: Draw a parallelogram labeled Input N to get the target limit from the user.
Process (Initialization): Draw a rectangle labeled i = 1 to start the counter at the first natural number.
Decision (Loop Condition): Draw a diamond shape labeled Is i <= N?.If Yes, draw a line pointing to the next output and process steps.If No, draw a line pointing directly to the End oval.
Output (Inside Loop): Draw a parallelogram labeled Print i to display the current number.
Process (Increment): Draw a rectangle labeled i = i + 1 to move to the next number, then draw a flow line pointing back up to the Decision diamond.
Flow Lines: Connect all shapes in sequence using arrows.

Example 3:

Sum of n natural numbers

# Take the input value for N from the user
n = int(input("Enter the value of N: "))
# Initialize the sum variable
total_sum = 0
# Loop from 1 up to n (n + 1 is exclusive)
for i in range(1, n + 1):
    total_sum += i
# Display the result using an f-string
print(f"The sum of first {n} natural numbers is: {total_sum}")

pseudo code:

START
    DECLARE n, i, sum
    sum = 0
    PRINT "Enter the value of N:"
    INPUT n
    FOR i = 1 TO n
        sum = sum + i
    END FOR
    PRINT "The sum of first ", n, " natural numbers is: ", sum
END

flow chart :

A flowchart maps these steps using standard geometric shapes:
Start/End: Draw an oval shape labeled Start at the top and End at the bottom.
Input: Draw a parallelogram labeled Input n to get the limit from the user.
Process (Initialization): Draw a rectangle labeled sum = 0 to reset the total before counting.
Decision (Loop): Draw a diamond shape labeled Is i <= n? to control the loop.
 If Yes, it connects to a rectangle labeled sum = sum + i and updates the counter (i = i + 1), then loops back to the diamond.
 If No, it exits the loop.
Output: Draw a parallelogram labeled Print sum to show the final result.
Flow Lines: Connect each shape in order using arrows.



Comments :

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.

Single line comments: #This is a comment
print("Hello, World!")

Multiline Comments:
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

16-09-2026

