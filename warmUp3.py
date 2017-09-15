#Erik Hansen
#9/15/2017
#warmUp3.py

num = int(input('Enter a number: '))
if num%3 == 0 and num%2 == 0:
    print(num, 'is divisible by both 2 and 3')
elif num%3 == 0:
    print(num, 'is divisible by 3')
elif num%2 == 0:
    print(num, 'is divisible by 2')
else:
    print(num, 'is not divisble by 2 or 3')


