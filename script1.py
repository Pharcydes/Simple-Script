# Program that inputs your name and two sets of numbers and returns either Hello World, 
# The second of two digits added together and your name as well.
# If not it prints Keep going
from unicodedata import digit
# variable name asking for your name to be store for later
name = input("Your name here ")
# input first number
input_a = input("a: ")
# input second number
input_b = input("b: ")
two_digit_number = (input_b)
# two variables for later on
a = 5
b = 3

# if else statement checking to see if a less than b print and if b and a are equal
if input_a < input_b:
    print("Hello World")
elif input_b == input_a:
    print(sum(int(digit) for digit in (two_digit_number)))
    

while a > 0:
    print("My name is")
    a -= 1
    if a == 1:
        continue
    print("Keep going")
