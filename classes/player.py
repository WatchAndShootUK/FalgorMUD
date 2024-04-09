import textwrap
from classes.inventory import Inventory
from classes.shape import Shape
from constants.debug import debug

class Player(object):
    def __init__(self,name,level,location_str,gender,race,stats,skills):
        self.name = name.title()
        self.conn = ''
        self.addr = ''
        self.level = level
        self.location_str = location_str
        self.gender = gender
        self.pronouns = []
        if self.gender == 'male':
            self.pronouns.append('he')
            self.pronouns.append('him')
            self.pronouns.append('his')
        else:
            self.pronouns.append('she')
            self.pronouns.append('her')
            self.pronouns.append('hers')
        self.race = race
        self.inv = Inventory(self)
        self.thread = ''
        self.hp, self.ep = self.set_hpep()
        self.max_hp, self.maxep = self.set_hpep()
        self.short = self.name.title() + " the " + self.race
        self.stats = stats
        self.skills = skills
        self.aliases = [name]
        self.parent = None
        self.shape = Shape(self)
        self.settings = Settings(self)
                          
    def send_message(self, message):
        if len(message) > 80:
            message = '    ' + message
        if debug:
            print(textwrap.fill(message, width=80))
        else:
            self.conn.send(message.encode() + b"\n")

    def display_long(self,player):
        player.send_message(self.name + " the " + self.race)
        if len(self.inv.get_inventory()) > 0:
            self.send_message(self.pronouns[0].title() + "is carrying the following items:")
            self.inv.show_inventory(player)
        else:            
            self.send_message(self.pronouns[0].title() + 'is empty handed.')
    
    def show_inv(self):
        if len(self.inv.get_inventory()) > 0:
            self.send_message("You are carrying the following items:")
            self.inv.show_inventory(self)
        else:            
            self.send_message("You are empty handed.")
    
    def kill(self):
        from classes.corpse import Corpse
        from constants.corpses import corpses
        
        self.parent.chat_room(self.aliases[0].title() + " has died.",[self])
        corpse = Corpse(self)
        self.parent.items.append(corpse)
        corpses.append(corpse)
        corpse.parent = self.parent
        self.parent.items.remove(self)

    def set_hpep(self):
        return int(50+self.level*10), int(50+self.level*10)
        
    def score(self):
        score1 = self.short
        score2 = "\nHP: " + str(self.hp) + '/' + str(self.max_hp) + " EP: " + str(self.ep) + "/" + str(self.maxep) + "                   Avg. Stats: " + str(self.stats.get_avg())
        score3 = "\nStrength: " + str(self.stats.strength) + "          Agility: " + str(self.stats.agility) + "            Charisma: " + str(self.stats.charisma)
        score4 = "\nConstitution: " + str(self.stats.constitution) + "      Coordination: " + str(self.stats.coordination) + "       Intelligence: " + str(self.stats.intelligence)        
        score5 = "\nLevel " + str(self.level) + " civillian, you are ageless!"
        self.send_message(score1 + score2 + score3 + score4 + score5)

class Settings:
    def __init__(self, parent):
        self.map_radius = 10
        self.parent = parent