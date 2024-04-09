from copy import deepcopy
from classes.room import Room
from constants.npcs import npcs
from constants.items import items

class CustomRoom(Room):
    def __init__(self):
        super().__init__(
            id = '158wa125',
            short = 'The West-Gate of Bree',
            long = 'Set before an old meeting of ways, the West-gate of Bree stands by the intersection of the Greenway and the Great East Road.  The town is visible against the western flank of Bree-hill rising high to the northeast.  What the hill does not protect is guarded by a deep dike running around the village with a thick hedge on the inner side forming a natural wall.  A wide causeway crosses over the dike, letting the eastern road continue upto and beyond the great gate piercing the hedge.  Behind the barrier is anelevated gatekeeper lodge with a window looking out over the roads.',
)
        self.exits = {'e':'100br106'}
        for obj in [npcs['a town guard'],npcs['a town guard'],npcs['an ugly orc'],items['a torch']]:
            self.append(deepcopy(obj)),
        
          
        self.special_commands = {
            'punch sign': self.punch_sign
        }        
        self.whip_in = True
    
    def punch_sign(self, player):
        if self.whip_in:
            self.whip_in = False
            player.send_message('You punch the big sign and dislodge something that was balancing on top of it! It falls on your head.')
            player.parent.append(items['a many-tailed whip'])
        else:
            player.send_message('You punch the big sign and hurt your hand.')
            player.hp -= 10
            
        
  