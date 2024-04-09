from classes.npc import NPC
from constants.items import items

class ThisNPC(NPC):
    def __init__(self):
        super().__init__(
            short='a town guard',
            long='This is a faithful guard who protects Bree.',
            aliases=['guard','town guard'],
            level=10
        )
        self.inv.hands.append(items['a polished cudgel'])
        self.inv.weapon = items['a polished cudgel']
        
        baldric = items['a simple leather baldric']
        baldric.items.append(items['a sturdy sword'])
        baldric.short = 'a simple leather baldric containing a sword'
        shield = items['a brown buckler']
        self.inv.append(baldric,'wearing')
        self.inv.append(shield,'wearing')
        
        
        