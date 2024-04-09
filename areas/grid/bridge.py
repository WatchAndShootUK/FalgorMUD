from copy import deepcopy
from classes.room import Room
from constants.npcs import npcs
from constants.items import items

class GenericGridRoom(Room):
    def __init__(self,id):
        super().__init__(
            id = id,
            short = 'The bridge',
            long = 'Vast rolling forest as far as you can see')
            
        
  