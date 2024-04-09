import textwrap
from utils.get_direction import GetDirection
from utils.proper import proper


class Room(object):
    def __init__(self,id,short,long):
        self.id = id
        self.short = short
        self.long = long
        self.items = []
        self.exits = {}
    
    def remove (self,item):
        if item in self.items:
            self.items.remove(item)
               
    def append(self,item):    
        # If living thing then announce entry  
        if hasattr(item,'hp'):
            self.chat_room(item.name.title() + ' enters.')
            self.display_short(item)            
        # Add item to self
        self.items.insert(0,item)
        # Remove item from previous parent
        if item.parent:
            item.parent.items.remove(item)
        # Set parent
        item.parent = self
                
            
    def chat_room(self,message,apart_from = []):
        # Send message to everyone in the room, use 'apart_from' if you don't want to broadcast to certain members.
        for item in self.items:
            if item not in apart_from:
                item.send_message(message)
            
    def display_short(self, player):     
        player.send_message(self.short + '(' + self.exit_str(self.exits,False) + ')')
        self.display_items(player)
        
    def display_long(self, player):        
        player.send_message(self.long)
        player.send_message("    The only obvious exits are " +  self.exit_str(self.exits,True) + ".")
        self.display_items(player)
        
    def display_items(self,player):
        for item in self.items:
            if item is not player:
                player.send_message(" " + proper(item.short))
            
    def exit_str(self, exits, full):
        new_exits = []
        for exit in exits:
            if full:
                new_exits.append(GetDirection(exit)())
            else:
                new_exits.append(exit)
        
        exit_str = ''
        i = 1
        if len(new_exits) > 1:
            for exit in new_exits:
                if i == len(new_exits):
                    divider = ' and '
                else:
                    divider = ', '
                exit_str = exit_str + divider + exit
                i += 1
            exit_str = exit_str[2:]
        else:
            for exit in new_exits:
                exit_str = exit
        return exit_str

