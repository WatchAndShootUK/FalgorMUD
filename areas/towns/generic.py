from classes.room import Room

class GenericRoom(Room):
    def __init__(self,id,town_name = None):
        super().__init__(
            id = id,
            short = 'A room in ' + town_name.title() if town_name else 'A room',
            long = 'A generic room.')
            
        
  