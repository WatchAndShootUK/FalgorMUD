from importlib import util
import os

rooms = {}

class LoadRooms:
    def __init__(self):
        for root, _, files in os.walk('areas'):
            for file in files:
                if file.endswith('.py'):
                    full_path = os.path.join(root, file)
                    spec = util.spec_from_file_location(file, full_path)
                    module = util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    for name in dir(module):
                        obj = getattr(module, name)
                        if hasattr(obj, '__class__') and obj.__class__.__name__ == 'type' and name == 'CustomRoom':
                            thisRoom = obj()
                            rooms[thisRoom.id] = thisRoom
                            
        for root, _, files in os.walk('areas'):
            for file in files:
                if file.endswith('.py'):
                    full_path = os.path.join(root, file)
                    spec = util.spec_from_file_location(file, full_path)
                    module = util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    for name in dir(module):
                        obj = getattr(module, name)
                        if hasattr(obj, '__class__') and obj.__class__.__name__ == 'type' and name in ['GridMap','TownMap']:
                            thisMap = obj()
                            LoadMap(thisMap,name)
        
class LoadMap:
    from areas.towns import street, shop, auction, inn, tavern, generic as genericTown
    from areas.grid import forest,generic as genericGrid,plains,road,rocky_ground, bridge
    
    def __init__(self,input_map,map_type):
        self.id = input_map.id
        self.map = input_map.map_array
        self.width = input_map.width
        self.height = input_map.height   
        self.name = input_map.map_name     
        self.map_type = map_type
        self.scan_map()
    
    exit_chars = ['-','\\','/','|']
    
    town_room_types = {
                  '+': street.GenericRoom,
                  's': shop.GenericRoom,
                  'a': auction.GenericRoom,
                  'i': inn.GenericRoom,
                  'o': genericTown.GenericRoom,
                  'b': tavern.GenericRoom,
                  'x': genericTown.GenericRoom}
    grid_room_types = {                  
                  '.': plains.GenericGridRoom,
                  '+': road.GenericGridRoom,
                  '%': forest.GenericGridRoom,
                  '^': rocky_ground.GenericGridRoom,
                  '*': genericGrid.GenericGridRoom,
                  ':': genericGrid.GenericGridRoom,
                  '\'': genericGrid.GenericGridRoom,
                  'O': genericGrid.GenericGridRoom,
                  '=': bridge.GenericGridRoom}
    
    def scan_map(self):
        # This function scans all rooms in a map and tries to create a new Room object for each.
        row = 0
        column = 0
        for line in self.map:
            for char in line:
                if char not in [' ','-','\\','/','|','~']:
                    self.create_room (char,column,row)
                column += 1
            row += 1
            column = 0
    
    def create_room(self, room_type, column,row):
        # This function sets the room UID and if the room doesnt already exist in dir, creates a Room object based on the room_type str.
        uid = str(column) + self.id + str(row)
        if uid not in rooms:
            if self.map_type == 'TownMap':
                thisRoom = self.town_room_types[room_type](uid,self.name)
            elif self.map_type == 'GridMap':
                thisRoom = self.grid_room_types[room_type](uid)                
        else:
            thisRoom = rooms[uid]
        new_exits = self.link_room(uid,column,row) if self.map_type == 'TownMap' else self.get_exits(column,row,self.grid_room_types)
        for direction,destination in new_exits.items():
            if direction not in thisRoom.exits:
                thisRoom.exits[direction] = destination
        rooms[uid] = thisRoom           
       
                
    def link_room(self, id, column, row):
        direction_mapping = {
            'e': (0, 1),  
            'w': (0, -1),  
            'n': (-1, 0), 
            's': (1, 0),  
            'nw': (-1,-1),
            'ne': (-1,1),
            'sw':(1,-1),
            'se':(1,1)
        }
        return_exits = {}

        exits = self.get_exits(column, row, self.exit_chars)
        for exit in exits:
            if exit in direction_mapping:
                delta_row, delta_col = direction_mapping[exit]
                temp_row, temp_col = row + delta_row, column + delta_col

                while 0 <= temp_row < self.height and 0 <= temp_col < self.width \
                        and self.map[temp_row][temp_col] in self.exit_chars:
                    temp_row += delta_row
                    temp_col += delta_col

                if exit in ['n', 's']:
                    return_exits[exit] = str(column) + ''.join(char for char in id if not char.isdigit()) + str(temp_row)
                elif exit in ['nw','ne','sw','se']:
                    return_exits[exit] = str(temp_col) + ''.join(char for char in id if not char.isdigit()) + str(temp_row)
                else:
                    return_exits[exit] = str(temp_col) + ''.join(char for char in id if not char.isdigit()) + str(row)

        return return_exits
           
    def get_exits(self,column,row,exit_chars):
        exits = {}
        if self.map[row][column+1] in exit_chars:
            exits['e'] = '' if self.map_type == 'TownMap' else str(column+1) + self.id + str(row)
        if self.map[row][column-1] in exit_chars:
            exits['w'] = '' if self.map_type == 'TownMap' else str(column-1) + self.id + str(row)
        if self.map[row+1][column] in exit_chars:
            exits['s'] = '' if self.map_type == 'TownMap' else str(column) + self.id + str(row+1)
        if self.map[row-1][column] in exit_chars:
            exits['n'] = '' if self.map_type == 'TownMap' else str(column) + self.id + str(row-1)
        if self.map[row-1][column+1] in exit_chars:
            exits['ne'] = '' if self.map_type == 'TownMap' else str(column+1) + self.id + str(row-1)
        if self.map[row-1][column-1] in exit_chars:
            exits['nw'] = '' if self.map_type == 'TownMap' else str(column-1) + self.id + str(row-1)
        if self.map[row+1][column+1] in exit_chars:
            exits['se'] = '' if self.map_type == 'TownMap' else str(column+1) + self.id + str(row+1)
        if self.map[row+1][column-1] in exit_chars:
            exits['sw'] = '' if self.map_type == 'TownMap' else str(column-1) + self.id + str(row-1)
        return exits
        
        
        
            
        