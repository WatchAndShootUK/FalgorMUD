from classes.item import Item,Weapon,Armour

class ThisItem(Item):
    def __init__(self):
        super().__init__(
            short='a sturdy sword',
            long='This is a sturdy sword used for protecting Bree.',
            aliases=['sword','sturdy sword']
        )    
        self.weapon = Weapon(25,self)