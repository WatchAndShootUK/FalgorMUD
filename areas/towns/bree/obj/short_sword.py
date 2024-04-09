from classes.item import Item,Weapon,Armour

class ThisItem(Item):
    def __init__(self):
        super().__init__(
            short='a short sword',
            long='This is a sword used for stabbing things.',
            aliases=['sword','short sword']
        )    
        self.weapon = Weapon(10,self)