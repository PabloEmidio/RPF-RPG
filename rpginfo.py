class RPGInfo:
    
    author = 'Anonymous'
    
    @staticmethod
    def welcome():
        print('Welcome to RPG game')
        
    
    @staticmethod
    def info():
        print('Made using OOP RPG game creator (c) me')
        
        
    @classmethod
    def credits(cls):
        print('Thank you for playing')
        print('Created by ' + cls.author)