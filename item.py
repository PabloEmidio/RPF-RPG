class Item:
    
    def __init__(self, item_name, item_description):
        self.name = item_name
        self._description = item_description
        
    def __repr__(self):
        return self.name
    
    @property    
    def description(self):
        return self._description
    
    @description.setter
    def description(self, item_description):
        self._description = item_description


    def describe(self):
        print('_' * 40 + '\n')
        print(f'Here has a {self.name}, it serves {self.description}')
        print('_' * 40 + '\n')