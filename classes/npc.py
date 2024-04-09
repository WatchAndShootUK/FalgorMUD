
from classes import inventory,shape,skills,stats


class NPC(object):
    def __init__(self,short,long,aliases,level):
        self.short = short
        self.long = long
        self.aliases = aliases
        self.name = aliases[0].title()
        self.inv = inventory.Inventory(self)
        self.in_combat = False
        self.skills = self.get_stats_skills(skills.Skills,level)
        self.stats = self.get_stats_skills(skills.Skills,level)
        self.parent = None
        self.shape = shape.Shape(self)
        self.max_hp = 40+(level*10)
        self.hp = self.max_hp
                   
    def get_stats_skills(self,classType,level):
        i = level*5
        if isinstance(classType, stats.Stats):
            return stats.Stats(i,i,i,i,i,i)
        else:
            return skills.Skills(i,i,i,i,i,i)
            
    def display_long(self,player):
        player.send_message(self.long)
        player.send_message('')
        if len(self.inv.get_inventory()) > 0:
            player.send_message(self.aliases[0].title() + " is carrying the following items:")
            self.inv.show_inventory(player)
        else:            
            player.send_message(self.aliases[0].title() + ' is empty handed.')
            
        player.send_message('') 
        player.send_message('Average stats: ' + str((self.stats.get_avg() + self.skills.get_avg())/2))
        if self.in_combat:
            player.send_message(self.short.capitalize() + " is fighting!!") 
        else:
            player.send_message(self.short.capitalize() + " isn't fighting anyone.")    
    
    def kill(self):
        from classes.corpse import Corpse
        from constants.corpses import corpses
        
        self.parent.remove(self)
        self.parent.chat_room(self.aliases[0].title() + " has died.")
        
        corpse = Corpse(self)
        self.parent.append(corpse)
        corpses.append(corpse)
        
    def send_message(self,message):
        message = message


