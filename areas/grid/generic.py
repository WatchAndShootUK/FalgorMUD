from classes.room import Room

class GenericGridRoom(Room):
    def __init__(self,id):
        super().__init__(
            id = id,
            short = 'A room',
            long = 'A generic room')
            
        
  