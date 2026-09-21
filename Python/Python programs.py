
#1.Accept two numbers and find their sum.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
total_sum = num1 + num2
print("The sum is:", total_sum)

#2.find sum and product of two numbers 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
product_result = num1 * num2
print(f"The sum of {num1} and {num2} is: {sum_result}")
print(f"The product of {num1} and {num2} is: {product_result}")

#3.Test whether a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an Even number.")
else:
    print(f"{num} is an Odd number.")

#4 Determine whether a number is zero, positive, or negative.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"
print(check_number(5))   # Output: Positive
print(check_number(-3))  # Output: Negative
print(check_number(0))   # Output: Zero

# 5 .Display numbers from 1 to 10 using a while loop.
i = 1
while i <= 10:
    print(i)
    i += 1

#6 Display even numbers between m and n
m = int(input("Enter m: "))
n = int(input("Enter n: "))
start = min(m, n)
end = max(m, n)
if start % 2 != 0:
    start += 1
for i in range(start, end + 1, 2):
    print(i)


17-9-2024
#7 Take two numbers as input and print the larger number. If both are equal, print "Equal".
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num1 > num2:
    print(num1)
elif num2 > num1:
    print(num2)
else:
    print("Equal")

#8 Take three numbers as input and find the largest of the three without using max().
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number is: {largest}")

#9Take an integer n and calculate its factorial using a loop. Example: 5 → 120
def calculate_factorial(n):
    # Handle the negative edge case
    if n < 0:
        return "Undefined for negative numbers"
        
    result = 1
    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        result *= i
    return result
print(calculate_factorial(5))  # Output: 120

#10  Take an integer and print its reverse.
Example: 12345 → 54321


num = int(input("Enter an integer: "))
reversed_num = int(str(num)[::-1])
print("Reversed number:", reversed_num)

#11 for string  Take string input from the user

r = input("Enter a string: ")
# Reverse the string using slicing [:: -1]
reversed_r = r[::-1]
# Print the reversed string
print(reversed_r)

#12 Check whether a given number is prime or not. Example:.py

def is_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
    
    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False  # Found a factor, so it is not prime
            
    return True  # No factors found, it is prime

# Example usage:
number_to_check = 29

if is_prime(number_to_check):
    print(f"{number_to_check} is a prime number.")
else:
    print(f"{number_to_check} is not a prime number.")


#13.Take n from the user and print the sum of numbers from 1 to n.
n = int(input("Enter a number (n): "))

if n < 1:
    print("Please enter a positive integer.")
else:
    total_sum = 0
    # Loop from 1 to n (range is exclusive of the stop value, so we use n + 1)
    for i in range(1, n + 1):
        total_sum += i
        
    print(f"The sum of numbers from 1 to {n} is: {total_sum}")
