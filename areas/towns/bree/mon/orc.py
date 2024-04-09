from classes.npc import NPC
from constants.items import items

class ThisNPC(NPC):
    def __init__(self):
        super().__init__(
            short='an ugly orc',
            long='This is a disgusting Orc, it should be killed!',
            aliases=['orc','ugly orc'],
            level=5
        )
        self.inv.hands.append(items['a short sword'])
        self.inv.weapon = items['a short sword']