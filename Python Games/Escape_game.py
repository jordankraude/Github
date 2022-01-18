'''
05 Prove: Story
CSE 110
Author: Jordan Kraude

Purpose: Make a program that takes inputs and puts
them into a story with multiple choices.
'''
#You should note that I didn't label all of the versions where the
#story just ends because the user puts something else other than
#what was allowed

#Instructions
print ('This is a adventure role playing game. You will be put into scenarios and you '
'need to make choices that will lead to new scenarios. Type one of the words that is in '
'all caps to move on. (EXP: RUN or HIDE, type "run" or "hide"). Try to win!! ')
print ('')

# Story line start
choice = input('You wake up in a dark spooky house. You have no light. '
'You have no idea how you got here...'
'what do you do? Do you look for a LIGHT or a WEAPON? ')
print('')

#Story line version 1
if choice.lower() == 'light':
    story_line1_choice1 = input('You spend 10 minutes looking for a light. In the meantime '
    'you hear many strange sounds. Eventually you finally find a light. '
    'You turn on the light and light up the room to find spiders everywhere. '
    'What do you do? RUN or STAY CALM? ')
    print('')

    #Story line version 1.1
    if story_line1_choice1.lower() == 'run':
        story_line1_choice_1a = input ('You run through the house looking for a exit making lots of '
        'commotion. You find some wooden stairs heading upstairs. Do you go UP or stay DOWN? ')
        print ('')

        #Story line version 1.1a
        if story_line1_choice_1a.lower() == 'up':
            story_line1_choice_2a = input ('You head upstairs and as you are half way up the wooden stairs '
            'the floorboard break from under you and you hit your head knocking you unconscious. When you '
            'wake up you find yourself in a hidden basement with tunnels. You point the light around and '
            'try to orient yourself. You see a two ways to go. One way heading to the right seems like it '
            'has light coming out at the end while the other leads into pitch black. Which way do you choose? '
            'Pitch BLACK or the LIGHT? ')
            print ('')

            #End Number 1
            if story_line1_choice_2a.lower() == 'black':
                print ('You walk down the end of the tunnel and you never see the light of day again. It takes you '
                'some time to realize what happened. You had actually died when you fell from the stairs. You chose '
                'to live in darkness for your afterlife... THE END')

            #End Number 2
            elif story_line1_choice_2a.lower() == 'light':
                print ('You walk down the tunnel and the further you go the lighter it gets. You never reach the end.. '
                'You realize that you had actually died from falling and that this is heaven you chose correctly to chose '
                'the right. ALWAYS CHOSE THE RIGHT! THE END ')
                print ('')

            else:
                print ('You have died...')

        #Story line version 1.1b
        elif story_line1_choice_1a.lower() == 'down':
            story_line1_choice_2b = input ('You choose to stay down and stay on the alert. You continue '
            'exploring the house and turn a corner that leads to a massive hallway with a door at the end. '
            'You then hear a gigantic roar from behind you. You can choose to either RUN down the hallway '
            'and open the door or TURN around and face what made that noise. What do you do?')

            #End Number 3
            if story_line1_choice_2b.lower() == 'run':
                print ('You run down the hallway and you throw open the door and you find that this door '
                'leads you outside. You escaped the house and now you need to find out how to get home.'
                'TO BE CONTINUED...')
            
            #End Number 4
            elif story_line1_choice_2b.lower() == 'turn':
                print ('You turn around just in time to see something with fangs come down around you. You '
                'never get to see what got you but you got got... You have died... THE END')
            
            else:
                print ('You have died...')

        else:
            print ('You have died...')

    #Story line version 1.2
    elif story_line1_choice1.lower() == 'stay calm':
        story_line1_choice_1b = input ('You keep your cool and you take a better look around the room '
        'that\'s when you notice that there is a window leading to the outside. '
        'You can BREAK the window or head into the KITCHEN. What do you do? ')
        print ('')

         #Story line version 1.2c
        if story_line1_choice_1b.lower() == 'break':
            story_line1_choice_2c = input ('You run over to the window and you shatter the glass which '
            'makes a very loud noise. You hear something make a thump from the other room.. Do you '
            'INVESTIGATE or do you LEAVE through the window? ')
            print ('')

            #End Number 5
            if story_line1_choice_2c.lower() == 'investigate':
                print ('You head over to where that thump sound was made to find a dead body there. You '
                'move a little bit closer to see what the heck happened.. That\'s when you find out that '
                'it wasn\'t a dead body.. It jumped up and grabbed you by the neck and bit you. You got '
                'got by a vampire... You have died... THE END')

            #End Number 6
            elif story_line1_choice_2c.lower() == 'leave':
                print ('You say nope to investigating what that sound was and you outie.. You jump out the '
                'window to breathe fresh air. You escaped the house and now you need to find out how to get home.'
                'TO BE CONTINUED...')

        #Story line version 1.2d
        elif story_line1_choice_1b.lower() == 'kitchen':
            story_line1_choice_2d = input ('You find a knife sitting on the counter as soon as you walk in. '
            'That\'s when you notice a dark figure in the corner of the room with sunken eyes.. It makes a wailing '
            'moan. What do you do? Do you RUN or do you take a stand and FIGHT or do you PRAY? ')
            print ('')

            #End Number 7
            if story_line1_choice_2d.lower() == 'run':
                print ('You run out of the room as you run you take glances back to see it following you. It '
                'moves fast and you see it better. It is completely deformed. You see the window from earlier '
                '(if only you had chosen the window earlier..) and make a dash for it. You never make it.. '
                'You got got by a ghoul... You have died... THE END ')

            #End Number 8
            elif story_line1_choice_2d.lower() == 'fight':
                print ('--Okay tough guy-- Wrong move... You got got by a ghoul. You have died... THE END')
            
            #End Number 9
            elif story_line1_choice_2d.lower() == 'pray':
                print ('You pray with all of your might as you hear it get closer to you. You feel it jump on you '
                'and that\'s when you jump out of your bed.. Oof you were just dreaming, thank goodness... THE END')
            
            else:
                print ('You have died...')

        else:
            print ('You have died...')
    else:
        print ('You have died...')

#Story line version 2    
elif choice.lower() == 'weapon':
    story_line2_choice_1 = input ('You spend 10 minutes looking for a weapon. In the meantime '
    'you hear many strange sounds. Eventually you finally find a knife in a drawyer. '
    'You hear a door open in the house.. What do you do? INVESTIGATE or HIDE? ')
    print('')

    #Story line version 2.1
    if story_line2_choice_1.lower() == 'investigate':
        story_line2_choice_1a = input ('You head towards the source of the sound to find a door '
        'It is still pitch black so you can\'t see much at all.. You can\'t tell if someone is still '
        'there. Your senses say yes because a door wouldn\'t have opened by itself. You can STAY where '
        'you are or you can distrust your senses and try to OPEN the door. What do you do? ')
        print ('')

        #End Number 10
        if story_line2_choice_1a.lower() == 'open':
            print ('Luckily your senses were wrong. You make it to the door and open it to feel the cold '
            'air hit your face. You walk away thinking you must have been wrong about feeling someone was '
            'in the house with you as you hear the door slam shut again.. You escaped the house and now you '
            'need to find out how to get home. TO BE CONTINUED...')

        #End Number 11
        elif story_line2_choice_1a.lower() == 'stay':
            print ('Unluckily your senses were wrong. No one was by the door because he had actually worked '
            'his way behind you. You got got by a murderer... You have died... THE END')

        else:
            print ('You have died...')

    #Story line version 2.2
    elif story_line2_choice_1.lower() == 'hide':
        story_line2_choice_1b = input ('You choose to hide. There is only problem. You have no idea where '
        'to hide because you can\'t see anything... You have your knife in hand and you find a door knob. '
        'You open it to find a closet. You cover yourself with a bunch of clothes to hide yourself. You '
        'hear the closet door start to open. You need to make a decision. Do you choose to FIGHT or STAY '
        'hidden')
        print ('')

        #End Number 12
        if story_line2_choice_1b.lower() == 'fight':
            print ('You choose to fight. When the door opens you blindly lunge foward and stick your knife '
            'in it (whoever or what ever it is). You do it successfully as it falls back and lets out a groan '
            'in suprise. You see the door wide open that it came through and you reach the outside. You have '
            'escaped and now you just need to find your way back home. TO BE CONTINUED... ')

        #End Number 13
        elif story_line2_choice_1b.lower() == 'stay':
            print ('The door opens and you see something look for you.. Luckily it leaves. Unluckily it locks '
            'the closet door behind it. You got got through starvation and deprivation. You have died... THE END')
            
        else:
            print ('You have died...')

    else:
        print ('You have died...')

#Story line version 3.. (end/nothing)
else:
    print('You have died...')
    
