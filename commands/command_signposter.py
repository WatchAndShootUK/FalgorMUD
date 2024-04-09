import re
from commands import comm,inventory,kill,look,move,quit,remove,save,score,shape,who,map,teleport
from classes import itemmover
from utils.get_direction import GetDirection

class CommandSignposter():
    def __init__ (self,player,input):
        match = re.match(r'([a-z]+|[\^])\s?(.+)?',input)
        if match:            
            if input in player.parent.exits:
                self.commands['move'](player,input)
            elif input in GetDirection.brief_dirs or input in GetDirection.full_dirs:
                player.send_message('You can\'t go that way!')
            elif hasattr(player.parent, 'special_commands') and input in player.parent.special_commands:
                player.parent.special_commands[input](player)
            elif match.group(1) in self.commands:
                self.commands[match.group(1)](player,input)
            else:
                player.send_message('What?')
        
    commands = {
        'look': look.look,
        'l': look.look,
        'kill': kill.kill,
        'remove': remove.remove,
        '^': comm.comm,
        'get': itemmover.ItemMover,
        'drop': itemmover.ItemMover,
        'put': itemmover.ItemMover,
        'wear': itemmover.ItemMover,
        'wield': itemmover.ItemMover,
        'i': inventory.inventory,
        'inventory': inventory.inventory,
        'move': move.move,
        'quit': quit.quit,
        'save': save.save,
        'score': score.score,
        'shape': shape.shape,
        'who': who.who,
        'map': map.map,
        'teleport': teleport.teleport
    }