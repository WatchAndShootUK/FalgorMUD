from classes.item import Item,Weapon,Armour

class ThisItem(Item):
    def __init__(self):
        super().__init__(
            short='a brown buckler',
            long='A small brown shield, worn on the hand.',
            aliases=['buckler','brown buckler']
        )    
        self.armour = Armour(50,['shield'],self)