from os import system

class Room:
    
    number_of_rooms = 0
    enemy_died = 0
    
    def __init__(self, room_name):
        Room.number_of_rooms +=1
        
        self._name = room_name
        self.linked_rooms = {}
        self._description = None
        self._character = None
        self._item = None
    
    
    @classmethod
    def enemy_was_dying(cls):
        cls.enemy_died +=1
    
    @property
    def description(self):
        print(self._description)
    

    @description.setter
    def description(self, room_description):
        self._description = room_description
        
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, room_name):
        self._name = room_name
        
    @property
    def character(self):
        return self._character
    
    @character.setter
    def character(self, new_character):
        self._character = new_character
        
        
    @property
    def item(self):
        return self._item
    
    
    @item.setter
    def item(self, new_item):
        self._item = new_item
        
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name + " linked rooms :" + repr(self.linked_rooms))

    
    def get_details(self):
        system('clear')
        print(self.name, end='----> ')
        self.description
        if self.character is not None:
            self.character.describe()
            
        if self._item is not None:
            self._item.describe()

        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f'--> The {room.name} is {direction}')

            
    def move(self, direction):

        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print('\033[1;31mYou can\'t go that way\033[m')
            return self