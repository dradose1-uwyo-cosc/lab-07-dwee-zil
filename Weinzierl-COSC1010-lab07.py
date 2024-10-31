# Mak Weinzierl
# UWYO COSC 1010
# October 31, 2024
# Lab 07
# Lab Section: 12
# Sources: Textbook, w3schools.com

# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

while True:
    print("Hello! Please enter a number to calculate its factorial.")
    print("Make sure your number is a positive integer or zero.")
    print("Enter 'exit' to exit.")
    number_entered = input("Enter your number here: ")
    
    factorial = 1
    number = 1

    if number_entered.lower() == "exit":
        break
    elif not number_entered.isdigit():
        print(f"\nPlease enter a positive integer or zero.\n")
        continue
    elif number_entered == 0:
        pass
    else:
        while number <= int(number_entered):
            factorial *= number
            number += 1

    print(f"\nThe factorial of {number_entered} is {factorial}.\n")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 
  
num_sum = 0 
print("Hello! Please enter integer values to determine their sum.")
print("When you are done entering numbers, enter 'exit' and the final sum will be outputted.")
      
while True:
    number = input("Enter your number here: ")

    if number.lower() == "exit":
        print(f"\nYour final sum is {num_sum}.\n")
        break
    else: 
        if number.isdigit():
            num_sum += int(number)
        elif "-" in number:
            number = number.replace("-","")
            if number.isdigit():
                num_sum -= int(number)
            else: 
                print(f"\nPlease enter only integer values.\n")
        else:
            print(f"\nPlease enter only integer values.\n")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input

def check_digit(list):
    """Check if entries in a list are digits."""
    if not list[0].strip().isdigit() or not list[1].strip().isdigit():
        return "no"
    
def make_integer(list):
    """Make entries in a list integers."""
    for index in range(0,2):
        list[index] = int(list[index])

while True:
    print("Please enter an expression in the form 'operand operator operand' to find its value.")
    print("You may use the following operators: +,-,/,*,%")
    print("Enter 'exit' to exit.")
    expression = input("Please enter your expression here: ")

    if expression.lower() == "exit":
        break
    else:
        if "+" in expression:
            operands = expression.split("+")
            if check_digit(operands) == "no":
                print(f"\nPlease enter an expression in the form 'operand operator operand'.\n")
                continue
            make_integer(operands)
            answer = operands[0] + operands[1]
        elif "-" in expression:
            operands = expression.split("-")
            if check_digit(operands) == "no":
                print(f"\nPlease enter an expression in the form 'operand operator operand'.\n")
                continue
            make_integer(operands)
            answer = operands[0] - operands[1]
        elif "/" in expression:
            operands = expression.split("/")
            if check_digit(operands) == "no":
                print(f"\nPlease enter an expression in the form 'operand operator operand'.\n")
                continue
            make_integer(operands)
            answer = operands[0] / operands[1]
        elif "*" in expression:
            operands = expression.split("*")
            if check_digit(operands) == "no":
                print(f"\nPlease enter an expression in the form 'operand operator operand'.\n")
                continue
            make_integer(operands)
            answer = operands[0] * operands[1]
        elif "%" in expression: 
            operands = expression.split("%")
            if check_digit(operands) == "no":
                print(f"\nPlease enter an expression in the form 'operand operator operand'.\n")
                continue
            make_integer(operands)
            answer = operands[0] % operands[1]
        else:
            print(f"\nPlease enter an expression in the form 'operand operator operand'.\n")
            continue
        
        print(f"\nThe value of your expression is {answer}.\n")