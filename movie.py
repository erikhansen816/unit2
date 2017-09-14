#Erik Hansen
#9/14/2017
#movies.py - most scandalous movie allowed

age = int(input('Enter your age: '))
if age >= 18:
    print('You can watch rated R movies')
elif age >= 13:
    print('You can watch rated PG-13 movies')
else:
    print('You can watch rated PG movies')
