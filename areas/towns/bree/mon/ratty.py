from classes.npc import NPC
from constants.items import items

class ThisNPC(NPC):
    def __init__(self):
        super().__init__(
            short='ratty the goat',
            long='This goat is MONSTOROUS',
            aliases=['ratty','goat'],
            level=25
        )