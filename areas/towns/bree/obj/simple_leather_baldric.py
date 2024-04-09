from classes.item import Item,Weapon,Armour

class ThisItem(Item):
    def __init__(self):
        super().__init__(
            short='a simple leather baldric',
            long='A baldric for storing your sword.',
            aliases=['baldric','simple baldric','leather baldric']
        )    
        self.armour = Armour(1,['back'],self)
        self.container = True