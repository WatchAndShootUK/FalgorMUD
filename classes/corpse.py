from constants.corpses import corpses
from classes.item import Item
from classes.room import Room
from utils.proper import proper

class Corpse(Item):
    def __init__(self,npc):
        self.short = "Corpse of " + npc.short.lower()
        self.items = npc.inv.get_inventory()
        self.name = 'corpse'
        self.npc = npc
        self.parent = None
        self.rot = 0
        self.aliases = ['corpse', npc.name.lower() + ' corpse']
        self.container = True
        
    def display_long(self,player):
        player.send_message("This is the corpse of " + self.short.lower() + ".")
        if len(self.items) > 0:
            player.send_message("It contains:")
            for item in self.items:
                player.send_message(" " + proper(item.short))   
    
    def send_message(self,message):
        message = message 
           
    def rot_away(self):
        self.parent.items.remove(self)
        corpses.remove(self)
        if isinstance(self.parent,Room):
            self.parent.chat_room('The corpse completely rots away.')             
        if len(self.items) > 0:
            self.parent.items.extend(self.items)
        
    def corpse_heartbeat(self):
        self.rot += 1
        if self.rot > 15:
            self.short = "Decaying corpse of " + self.npc.short.lower()
            if self.rot > 30:
                self.rot_away()
            
