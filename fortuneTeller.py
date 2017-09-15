#Erik Hansen
#9/15/2017
#fortuneTeller.py - telling fortune based on color and number

color = str(input('Choose a color, either red or blue: '))
num = int(input('Choose a number between 1 and 4: '))

if color == 'blue' and num == 1:
    print('You will win the lottery when you turn 26 years old')
elif color == 'blue' and num == 2:
    print('You will live a very short and boring life')
elif color == 'blue' and num == 3:
    print('You will go to a great college but do nothing with your life... loser')
elif color == 'blue' and num == 4:
    print('You will become very close friends with lil pump Jet Ski and have an awesome life')
elif color == 'red' and num == 1:
    print('You will fall out of a plane while using the plane bathroom on your next flight')
elif color == 'red' and num == 2:
    print('You will become a billionaire but spend all of your money on in-app purchases for clash royale')
elif color == 'red' and num == 3:
    print('You will be  the first person to step foot on mars')
else:
    print('You will die tomorrow')