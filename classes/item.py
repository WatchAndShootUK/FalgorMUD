from utils.proper import proper


class Item(object):
    def __init__(self,short,long,aliases):
        self.short = short
        self.name = short.split()[-1]
        self.long = long
        self.items = []
        self.aliases = aliases
        self.parent = None
        
    def display_long(self,player):
        player.send_message(self.long)
        if hasattr(self, 'container'):
            if len(self.items) > 0:
                player.send_message("It contains:")
                for item in self.items:
                    player.send_message(proper(item.short))
            else:
                player.send_message('It\'s empty.')
        if hasattr(self,'armour'):
            if self.armour.worn:
                player.send_message(proper(self.short) + ' is currently being worn.')
            else:
                player.send_message(proper(self.short) + ' is currently not being worn.')
    
    def send_message(self,message):
        message = message
   
class Weapon(Item):
    def __init__(self,power,item):       
        self.power = power
        self.parent = item   
        self.wielded = False
                    
class Armour(Item):
    def __init__(self,power,body_parts,item):
        self.power = power
        self.parent = item
        self.body_parts = body_parts
        self.worn = False

