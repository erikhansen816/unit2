#Erik Hansen
#9/15/2017
#adventure.py - making an adventure

print('A bat bites you while you are sleeping and you wake up with supernatural agility and hate the light. You realize you are a vampire. After being a vampire for two days you start to crave blood. A human enters the cave to check on you')
ans1 = input('Do you bite his neck, yes or no?')
if ans1 == 'yes':
    print("When you bit the man's neck you hit his jugular vein and he died a slow and painful death in the cave. You panicked because you realized that people are gonna start looking for him. You plan to leave the cave when the sun goes down because you are too afraid to go out in the light. You accidentally fell asleep and when you woke up, you are surrounded by dozens of police officers. They took you to their station and sentenced you to life in prison for. You then spent the rest of your days sitting alone in solitary confinement so you don't hurt anyone else. You die at the age of 27. Very sad life")
else:
    print('The man thanks you for sparing his life and offers you a million dollars and a cure to being a vampire!')
    ans2 = input('Do you accept his offer, yes or no? ')
    if ans2 == 'yes':
        print('The vampire cure works and you went back to normal. You were very wealthy and your life was filled with exciting parties and it was great. Unfortunately, after about 6 months after the incident, a drug dealer attempted to rob you of all your money.')
        ans3 = input(' Do you give him the money, yes or no? ')
        if ans3 == 'yes':
            print("He takes all of your money but doesn't want you to report him to the police so he kills you and throws you in the connecticut river. Your body is never found")
        else:
            print('He gets mad that you said no so he murders you and takes all your money! No one notices that you are gone.')
    else: 
        print('The man leaves the cave and you are left with nothing. You live alone for several months without any contact to the outside world. You find animals around the cave at night to eat. After a while you get bored of this life and go back into civilization still as a vampire. You meet a casting agent and you turn into the next lead role in the Twilight Series. You live an awesome life and after 5 years of being the star, you find vampire cure and go back to normal. You are very wealthy and the rest of your life is incredible!')
    