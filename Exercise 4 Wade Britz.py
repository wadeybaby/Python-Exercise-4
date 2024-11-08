# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
fruits = ['Apple', 'Pear', 'Banana', 'Orange']
# TODO: Use a for loop to print each fruit in the list
print('List of fruits: ')
for fruit in fruits:
    print(fruit)

#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    count -= 1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
print('The first 10 square numbers: ')
for num in range(1 , 11):
    square = num **2
    print(f'{num} squared: {square}')

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
colours = ['Blue', 'Pink', 'Red', 'Black', 'Green']
# TODO: Use a for loop to select and print 3 random colors from the list
print('Randomly selected colours:')
for random_colour in range(3):
    random_colour = random.choice(colours)
#     print(random_colour)

#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# # TODO: Import the custom module and use its functions
import math_operations

# # TODO: Use a while loop to create a simple calculator
def calculator():
    print('Select an operation: ')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    return input('Enter choice (1/2/3/4)')
    
while True:
    choice = input('Enter your choice (1-4): ')

    if choice in ['1', '2', '3', '4']:
        try:    
            num1 = float(input('Enter first number: '))
            num2 = float(input('Enter second number: '))
        
            if choice == '1':
                 result = math_operations.add(num1, num2)
                 print(f'The result of {num1} + {num2} = {result}')
            elif choice == '2':
                result = math_operations.subtract(num1, num2)
                print(f'The result of {num1} - {num2} = {result}')
            elif choice == '3': 
                result = math_operations.multiply(num1, num2)
                print(f'The result of {num1} * {num2} is = {result}')
            elif choice == '4':
                result = math_operations.divide(num1, num2)
                print(f'The result of {num1} / {num2} = {result}')     

        except ValueError:
            print('Invalid input. Please enter numerical values.')
    else:
        print('Invalid choice. Please choose a valid operation')        
