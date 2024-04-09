from constants.items import LoadItems
from constants.npcs import LoadNPCs
from constants.rooms import LoadRooms

class StartMud:
    def __init__(self):
        LoadItems()
        LoadNPCs()
        LoadRooms()