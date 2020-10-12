from abc import ABC, abstractmethod

class Character(ABC):
    
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self._conversation = None
    
    @abstractmethod    
    def __repr__(self):
        return 'Character'
    
    def describe(self):
        print('_' * 40 + '\n')
        print(f'{self.name} is here! --> {self.description}')
        print('_' * 40 + '\n')
    
    @property
    def conversation(self):
        return self._conversation
    
    
    @conversation.setter
    def conversation(self, conversation):
        self._conversation = conversation
        
        
    def talk(self):
        if self.conversation is not None:
            print(f'{self.name} says: {self.conversation}')
        else:
            print(f'{self.name} doesn\'t want to talk to you')
            
            
    def fight(self):
        print(self.name + ' does\'t want to fight with you')
        return True
    
            
class Enemy(Character):
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self._weakness = None
        
        
    def __repr__(self):
        return 'Enemy'
        
        
    @property
    def weakness(self):
        print(self._weakness)
        
    
    @weakness.setter
    def weakness(self, weakness_name):
        self._weakness = weakness_name
        
        
    def fight(self, combat_item):
        if combat_item == self._weakness:
            print(f'You fend {self.name} off with the {combat_item}')
            return True
        else:
            print(f'{self.name} crushes you, puny adventurer')
            return False
        


class Friend(Character):
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        
    def __repr__(self):
        return 'Friend'
        
