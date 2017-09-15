#Erik Hansen
#9/15/2017
#insulter.py - giving insults

from random import randint

name = str(input('What is your name? '))
print(name)
num = randint(1,5)
if num == 1:
    print('You seem like the type of guy that pees sitting down')
elif num == 2:
    print('You. Are. A. Loser.')
elif num == 3:
    print('You have absolutely no friends! :)')
elif num == 4:
    print('Your birth certificate is an apology letter from the condom factory')
else:
    print('I hate your face.')

