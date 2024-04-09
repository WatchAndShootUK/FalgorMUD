from copy import deepcopy
from classes.room import Room
from constants.npcs import npcs
from constants.items import items

class CustomRoom(Room):
    def __init__(self):
        super().__init__(
            id = '102br106',
            short = 'The Bree town centre',
            long = 'Set before an old meeting of ways, the West-gate of Bree stands by the intersection of the Greenway and the Great East Road.  The town is visible against the western flank of Bree-hill rising high to the northeast.  What the hill does not protect is guarded by a deep dike running around the village with a thick hedge on the inner side forming a natural wall.  A wide causeway crosses over the dike, letting the eastern road continue upto and beyond the great gate piercing the hedge.  Behind the barrier is anelevated gatekeeper lodge with a window looking out over the roads.',)
    
        self.append(deepcopy(npcs['ratty the goat']))
        self.special_commands = {
            'pray to aragorn': self.anduril
        }        
        self.anduril = True
    
    def anduril(self, player):
        if self.anduril:
            self.anduril = False
            player.send_message('You pray to Aragorn and he appears out of the mist, forfilling your wildest fantasies. He smiles at you before handing you the reforged Narsil, now named Anduril - the Flame of the West.')
            player.parent.append(items['anduril, the Flame of the West'])
        else:
            player.send_message('He doesn\'t hear your prayers.')
        