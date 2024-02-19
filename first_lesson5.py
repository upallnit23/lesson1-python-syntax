import math

#Lesson 1 Assignment:Python Syntax
#Python Indentation Practice
#Task 1:Code Correction

weather = "sunny"

if weather == "sunny":
    print("Wear glasses!")
else:
    print("Take an unbrella!")

#Task 2:Your Mood Today

user_mood = input("Do you feel happy or sad today?")

if user_mood == "happy":
    print("That's great to hear!")
else:
    print("I hope your day gets better!")

#Task 3:Spotting Indentation Errors
    
mood = "excited"

if mood == "excited":
    print("Yay! Let's have fun.")
else:
    print("Let's find something fun to do!")

#Python Comments & Multi-line Practice
#Task 1:Create a Poem using Comments
    
#Python syntax is not so bad,
#When you practice it frequently.
#I hope to master it very soon,
#So that I can be free to learn more in it.
    
#Task 2: Multi-line Poem

"""Python is not so easy to learn.
    Neither is it so hard.
    Once mastered, 
    I will find it a yarn,
    Or better yet a tool to drum."""

#Task 3: Combining Single and Multi-line Comments

#This line is from my first poem
#Python syntax is not so bad,

#This line is from my multi-line poem
"""
Or better yet a tool to drum.
"""
#Python Naming Convention Practice

#Task 1:Code Correction

#pi_value = 3.14
#user_age = 25
#user_location = "New York"
#MAX_LIMIT = 1000

#Python Data Types and type() Function

#Task 1: Code Correction

variable_a = "Hello, World!"
variable_b = 23
variable_c = 3.14
variable_d = True

print(type(variable_a))
print(type(variable_b))
print(type(variable_c))
print(type(variable_d))

#Python Dynamic Typing Practice

#Task 1:Code Correction

dynamic_variable = "This is a string"
print(type(dynamic_variable))

dynamic_variable = 100
print(type(dynamic_variable))

dynamic_variable = 25.5
print(type(dynamic_variable))

#Arithmetic Operations in Daily Life

#Task 1: Grocery Store Math

groceries = 1.21 + 3.89 + 6.74
print(groceries)

#Task 2: Bank Interest

bank_interest = 600 * 0.02 * 1
print(bank_interest)

#Task 3:Area and Perimeter

area = 7 * 12
perimeter = 2 * 7 + 2 * 12

print(area)
print(perimeter)

#Understamding Assignments and Comparisons

#Task 1:Value Swapping

value1, value2 = 5, 8

print(value1)
print(value2)

if value1 > value2:
    print("value1 is greater than value2")
else:
    print("value2 is greater than value1")

value1, value2 = value2, value1

print(value1)
print(value2)

if value1 > value2:
    print("value1 is greater than value2")
else:
    print("value2 is greater than value1")

#Task 2:Perfect Square Checker

num1 = input("Enter a number") 
num2 = int(num1)

if type(num2) != float:
    print(num2)
    print(" is a perfect square")
else:
    print(num2) 
    print(" is not a perfect square ")

#Exploring Logical Operations and Precedence
    
#Task 1:Simple Logic Puzzles
    
henry, lucky = "cat", "dog"

if henry == "cat":
    print("henry is a cat")
else:
    print("henry is not a cat")

if henry == "cat" or "dog":
    print("henry is either a cat or dog")
else:
    print("henry is neither a cat nor dog")

if lucky == "cat" and "dog":
    print("lucky is a cat and a dog")
else:
    print("lucky is neither a cat nor a dog")

#Task 2:Validating Calculations
a = 15
b = 27

sum = a + b / a * b
sum1 = a + b / (a * b)

print(sum)
print(sum1)

#Task 3:Mix and Match

tal, age1 = "dog", 7
leon, age2 = "rabbit", 3

"""
tal and leon have a combined age of 10, and are either a dog
or a rabbit
"""
if (leon == "rabbit" or tal == "dog") and (age1 + age2 == 10):
    print("tal and leon are a dog or a rabbit, with a combined age of 10")
else:
    print("this did not work")
    