from room import Room
from character import Friend, Enemy
from rpginfo import RPGInfo
from item import Item
from time import sleep
from os import system

RPGInfo.welcome()
RPGInfo.info()
sleep(2)


bakpack = ['silver', 'cheese']


# add kitchen object in the game
kitchen = Room('Kitchen')
kitchen.description = 'The place that people cook food'

# add ballroom object in the game
ballroom = Room('Ball Room')
ballroom.description = 'The place that people go to dance'

# add dining hall object in the game
dining_hall = Room('Dining Hall')
dining_hall.description = 'The place that people eat them food'

# link the kitchen to the ballrom and dining hall
kitchen.link_room(ballroom, 'southwest')
kitchen.link_room(dining_hall, 'south')

# link the dining to the ballrom and kitchen
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'east')

# link the ballroom to the kitchen and dining hall
ballroom.link_room(kitchen, 'northeast')
ballroom.link_room(dining_hall, 'west')

# creating the first enemy and putting him in the dining hall
enemy = Enemy('Drake', 'A sweetie zumbie')
enemy.conversation = 'braaain, I want braaaain'
enemy.weakness = 'cheese'
dining_hall.character = enemy

# creating the second enemy and putting him in the ballroom
enemy_two = Enemy('David', 'A dangerous demon')
enemy_two.conversation = 'I want to take your soul'
enemy_two.weakness = 'silver'
ballroom.character = enemy_two


# creating a friendly person and putting in the kitchen
friend = Friend('jacob', 'A very friendly guy')
friend.conversation = 'I\'m just passing a time here'
kitchen.character = friend

knife = Item('knife', 'to kill people')
kitchen.item = knife


current_room = kitchen # creating the walk form starting in the kitchen
while True:
    
    print('\n')
    print(f'There are {Room.number_of_rooms} rooms to explorer')
    if current_room.character is not None:
        inhabitant = current_room.character
    if current_room.item is not None:
        hashere = current_room.item
    current_room.get_details()
    command = input('> ').lower()
    if command in ['south', 'west', 'north', 'east', 'southwest', 'northeast']:
        current_room = current_room.move(command) # to go to next room

    elif command == 'fight' and current_room.character is not None:
        
        if inhabitant.__str__() == 'Friend':
            inhabitant.fight()
            
        else:
            system('clear')
            print(f'Fight\' hours\nYou vs {inhabitant.name}')
            while True:
                print(f'Your itens are {bakpack}, choose one')
                combat_item = str(input('What\'s your combat item?\n> ')).lower()
                if combat_item in bakpack:
                    break
                print('Choose between your itens')
            if inhabitant.fight(combat_item):
                print(f'You killed {inhabitant}')
                Room.enemy_was_dying()
                if Room.enemy_died == 3:
                    system('clear')
                    print('ALL ENEMY WAS DYING, YOU WIN THE GAME')
                    print('\033[1;34mCONGLATULATIONS\033[m')
                    break

                current_room.character = None
            else:
                print('\033[1;33mGAMER OVER\033[m')
                break 
    
    
    elif command == 'talk' and current_room.character is not None:
        inhabitant.talk()
        if inhabitant.__str__() == 'Enemy':
            print('You went to talk with enemy and you died')
            print('\033[1;31mGAMER OVER\033[m')
            break
        
    elif command == 'take' and current_room.item is not None:
        takewhat = str(input('To take what?\n> ')).lower()
        if takewhat == hashere.name:
            bakpack.append(hashere.name)
            current_room.item = None
    elif command == 'itens':
        print(f'your itens are {bakpack}')
    else:
        print('Command invalid')

    
    input('\nPress ENTER to continue\n')



RPGInfo.credits()