from copy import deepcopy
from classes.room import Room
from constants.npcs import npcs
from constants.items import items

class GenericRoom(Room):
    def __init__(self,id,town_name = None):
        super().__init__(
            id = id,
            short = 'A street in ' + town_name.title() if town_name else 'A street',
            long = 'It\'s a street')
            
        
  