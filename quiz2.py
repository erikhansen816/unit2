#Erik Hansen
#9/25/2017
#quiz2.py - Quiz program on unit 2

num1 = int(input('Enter a number: '))
num2 = int(input('Enter a second number: '))
#This part determines which number is the biggest
if num1>num2:
    print('The first number is bigger')
elif num2>num1:
    print('The second number is bigger')
else:
    print('The numbers are the same')
#This part determines their divisibility by 3
if num1%3 == 0 and num2%3 == 0:
    print('Both are divisible by 3')
elif num1%3 == 0:
    print('The first is divisible by 3')
elif num2%3 == 0:
    print('The second is divisible by 3')
else:
    print('Neither are divisible by 3')
#This part asks for the product and determines if the answer is correct
product = int(input('What is the product of these two numbers? '))
if product == num1*num2:
    print('Correct')
else:
    print('Incorrect')
